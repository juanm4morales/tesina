#!/usr/bin/env python3
"""Joint OD / fixed-route assignment with conservative model service bounds.

This is a synthetic scenario revision, not independent demand calibration.
No SUMO or duarouter process is started here.
"""
from collections import defaultdict
from copy import deepcopy
from decimal import Decimal,getcontext
import heapq
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack
from build_mendoza_civit import ROOT,NETS,sha,write_json,write_xml

HERE=ROOT/'experiments/mendoza_scenario/results/mendoza_compact_flows_20261020'
NETWORK=NETS/'mendoza_civit_static.net.xml';ZONES=NETS/'mendoza_civit_static.taz.xml';SOURCE=NETS/'mendoza_civit_static.rou.xml'
HOT={'446118223#7':300,'-574183755#0':900,'-161265844#1':350,'227837259':250}


def route_pool(net,zones,pairs):
    edges={e.get('id'):e for e in net.findall('edge')};logic={t.get('id'):t for t in net.findall('tlLogic')}
    adj=defaultdict(list);edge_capacity={};movement_capacity={}
    for c in net.findall('connection'):
        src,dst=c.get('from'),c.get('to');tid=c.get('tl');lane=c.get('fromLane')
        if tid:
            i=int(c.get('linkIndex'));fraction=sum(float(p.get('duration'))*(1 if p.get('state')[i]=='G' else .3 if p.get('state')[i]=='g' else 0) for p in logic[tid].findall('phase'))/90
        else:fraction=.10 if c.get('state') in ('m','o') else 1.0
        adj[src].append((dst,c,fraction))
        movement_capacity[(src,dst,lane)]=1050*fraction
    for src,values in adj.items():
        lanes={}
        for dst,c,fraction in values:lanes[c.get('fromLane')]=max(lanes.get(c.get('fromLane'),0),1050*fraction)
        edge_capacity[src]=sum(lanes.values())
    specific=defaultdict(float)
    for (src,dst,lane),cap in movement_capacity.items():specific[(src,dst)]+=cap
    # Bounds are engineering hypotheses for the model, not measured field capacity.
    # They include short-receiver storage and a margin below observed saturation.
    capacities={('edge',e):v for e,v in edge_capacity.items()}
    for k,v in specific.items():capacities[('movement',)+k]=v
    for e,v in HOT.items():capacities[('edge',e)]=min(v,capacities.get(('edge',e),v))

    def fastest(sources,sinks,penalty,diversity):
        q=[];cost={};previous={}
        for src in sources:
            e=edges[src];v=min(13.89,max(float(l.get('speed')) for l in e.findall('lane')))
            d=float(e.find('lane').get('length'))/v;cost[src]=d;heapq.heappush(q,(d,src))
        while q:
            d,e=heapq.heappop(q)
            if d!=cost[e]:continue
            if e in sinks:
                path=[e]
                while e in previous:e=previous[e];path.append(e)
                return tuple(reversed(path)),d
            for dst,c,fraction in adj[e]:
                nxt=edges[dst];v=min(13.89,max(float(l.get('speed')) for l in nxt.findall('lane')))
                delay=(90*(1-fraction)**2/2) if c.get('tl') else (20 if fraction<1 else 0)
                extra=penalty*(120 if dst in HOT or dst=='249657488#2' else 0)+diversity.get(dst,0)
                nd=d+float(nxt.find('lane').get('length'))/v+delay+extra
                if nd<cost.get(dst,float('inf')):cost[dst]=nd;previous[dst]=e;heapq.heappush(q,(nd,dst))
        raise ValueError('unreachable OD')
    pools=[]
    for pair in pairs:
        found=[];diversity={}
        for penalty in [0,1,3,6,10]:
            path,cost=fastest(zones[pair[0]][0],set(zones[pair[1]][1]),penalty,diversity)
            if path not in [x['edges'] for x in found]:
                found.append({'edges':path,'generalized_cost':cost,
                              'length':sum(float(edges[e].find('lane').get('length')) for e in path)})
            for e in path:diversity[e]=diversity.get(e,0)+10
            if len(found)==3:break
        for p in found:p['edges']=list(p['edges'])
        pools.append(found)
    return pools,capacities


def build():
    getcontext().prec=40
    HERE.mkdir(exist_ok=True)
    if (HERE/'design.json').exists():raise FileExistsError('assignment is frozen')
    net=ET.parse(NETWORK).getroot();original=ET.parse(SOURCE).getroot()
    pairs=sorted({(f.get('fromTaz'),f.get('toTaz')) for f in original.findall('flow')})
    zones={z.get('id'):([s.get('id') for s in z.findall('tazSource')],[s.get('id') for s in z.findall('tazSink')]) for z in ET.parse(ZONES).getroot().findall('taz')}
    pools,capacities=route_pool(net,zones,pairs)
    variables=[(i,j,p) for i,pool in enumerate(pools) for j,p in enumerate(pool)]
    count=len(variables);od=np.zeros((len(pairs),count));inc=np.zeros((len(capacities),count));keys=list(capacities)
    ki={k:i for i,k in enumerate(keys)}
    for col,(i,j,p) in enumerate(variables):
        od[i,col]=1
        for a,b in zip(p['edges'],p['edges'][1:]):
            inc[ki[('edge',a)],col]+=1;inc[ki[('movement',a,b)],col]+=1
    cap=np.array([capacities[k] for k in keys]);cost=np.array([v[2]['length'] for v in variables]);solutions=[]
    output=deepcopy(original)
    for f in output.findall('flow'):output.remove(f)
    flows={f.get('id'):deepcopy(f) for f in original.findall('flow')};ledger=[]
    for hour in range(12):
        ff={(f.get('fromTaz'),f.get('toTaz')):f for f in original.findall('flow') if int(float(f.get('begin')))//3600==hour}
        base=np.array([float(ff[p].get('period')[4:-1])*3600 for p in pairs])
        # Exact hourly total, conserved support, no banished OD pair. Far fewer
        # crossings and conservative service constrain the new route assignment.
        lower=.2*base;upper=3*base
        for i,p in enumerate(pairs):
            if p[0]=='7':upper[i]=.5*base[i]
            if p[0]=='10':upper[i]=.75*base[i]
            if p[0]=='34':upper[i]=.25*base[i]
        # Variables: path flows and absolute OD changes. Prefer minimal relocation;
        # secondary path cost discourages detours without pretending a DUE solution.
        n=len(pairs);zeros=np.zeros((len(cap),n))
        aub=np.vstack([np.c_[inc,zeros],np.c_[od,-np.eye(n)],np.c_[-od,-np.eye(n)],
                       np.c_[od,np.zeros((n,n))],np.c_[-od,np.zeros((n,n))]])
        bub=np.r_[cap,base,-base,upper,-lower]
        objective=np.r_[.00005*cost,np.ones(n)]
        eq=np.r_[np.ones(count),np.zeros(n)][None,:]
        result=linprog(objective,A_ub=aub,b_ub=bub,A_eq=eq,b_eq=[sum(base)],bounds=(0,None),method='highs')
        if not result.success:
            write_json({'status':'offline_infeasible','hour':hour,'solver_message':result.message},HERE/'infeasible.json');raise RuntimeError(result.message)
        x=np.maximum(0,result.x[:count]);new=od@x
        rates=[(Decimal(str(float(v)))/3600).quantize(Decimal('0.000000000000000001')) for v in new]
        total=sum(Decimal(f.get('period')[4:-1]) for f in ff.values());rates[int(np.argmax(new))]+=total-sum(rates)
        for i,pair in enumerate(pairs):
            f=flows[ff[pair].get('id')];f.attrib.pop('fromTaz');f.attrib.pop('toTaz')
            did=f'paths_{pair[0]}_{pair[1]}_h{hour}'
            dist=ET.SubElement(output,'routeDistribution',id=did)
            choices=[(j,p,float(x[col]/new[i])) for col,(ii,j,p) in enumerate(variables) if ii==i and x[col]>1e-8]
            assert choices and new[i]>0
            for j,p,weight in choices:ET.SubElement(dist,'route',edges=' '.join(p['edges']),probability=f'{weight:.16g}')
            f.set('route',did);f.set('period',f'exp({rates[i]:.18f})')
            ET.SubElement(f,'param',key='study.originTAZ',value=pair[0]);ET.SubElement(f,'param',key='study.destinationTAZ',value=pair[1])
            ledger.append({'flow':f.get('id'),'origin':pair[0],'destination':pair[1],
                           'old_rate':ff[pair].get('period'),'new_rate':f.get('period'),'route_distribution':did})
        solutions.append({'hour':hour,'total_expected':float(sum(new)),'moved_fraction':float(np.maximum(new-base,0).sum()/sum(base)),
                          'expected_vkt':float(cost@x/1000),'maximum_capacity_ratio':float(np.max(inc@x/cap))})
    for f in sorted(flows.values(),key=lambda f:(float(f.get('begin')),f.get('id'))):output.append(f)
    route=HERE/'compact.rou.xml';write_xml(output,route)
    assert len(ET.parse(route).getroot().findall('flow'))==6204
    write_json({'pairs':[list(p) for p in pairs],'route_pools':pools,
                'capacities':[{'key':list(k),'expected_veh_per_hour_bound':v} for k,v in capacities.items()],
                'routing':'fixed native route distributions, no online rerouting or DUA claim',
                'capacity_caveat':'1050 veh/h times green fraction; permissive fraction .3; uncontrolled minor fraction .1; development assumptions'},HERE/'profile.json')
    write_json(ledger,HERE/'ledger.json')
    previous=json.loads((ROOT/'experiments/mendoza_scenario/results/mendoza_flow_balance_20261020/design.json').read_text())
    adapter=ROOT/'experiments/mendoza_scenario/run_mendoza_compact_flows.py'
    shared=ROOT/'experiments/mendoza_scenario/run_mendoza_flow_balance.py'
    design={'candidate':'compact','status':'frozen_pending_screen','nominal_daily':220000,
            'builder_sha256':sha(__file__),'adapter_sha256':sha(adapter),'shared_runner_sha256':sha(shared),
            'frozen_network_sha256':sha(NETWORK),'frozen_zones_sha256':sha(ZONES),
            'source_route_sha256':sha(SOURCE),'local_gates':previous['local_gates'],
            'candidates':[{'id':'compact','status':'frozen','route':str(route.relative_to(ROOT)),'sha256':sha(route)}],
            'solutions':solutions,'contract':{'hourly_totals':'unchanged','expected_12h':152168.7538800684,
                'origins_and_destinations':'synthetically_redistributed','TAZ28':'no_longer_fixed_in_this_new_revision',
                'OD_bounds':[.2,3],'source_7_max_ratio':.5,'source_10_max_ratio':.75,'source_34_max_ratio':.25,
                'signal_changes':0,'native_poisson':True,'flow_count':6204,'route_assignment':'fixed_distributions',
                'rationale':'prior dynamic assignment invalidated route exposure forecasts; remove that uncontrolled assignment variation'},
            'budget':{'4h':1,'12h':1,'2h':1,'seed':104729,'retries':0}}
    write_json(design,HERE/'design.json')
    print(json.dumps({'paths':count,'solutions':solutions},indent=2))


if __name__=='__main__':build()
