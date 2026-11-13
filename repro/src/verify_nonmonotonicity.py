from collections import deque
from itertools import combinations

def vertices(n):
    return [format(x, f'0{n}b') for x in range(1<<n) if not (x & (x<<1))]

def bfs(graph,start):
    q=deque([start]); d={start:0}
    while q:
        v=q.popleft()
        for u in graph[v]:
            if u not in d:d[u]=d[v]+1;q.append(u)
    return d

def signatures(V,L):
    S=set(L);adj={x:[y for y in V if sum(a!=b for a,b in zip(x,y))==1] for x in V}
    ds={w:bfs(adj,w) for w in L}
    results={}
    for x in V:
        if x not in S:
            key=tuple(sorted(ds[w][x] for w in L))
            results.setdefault(key,[]).append(x)
    return results
V=vertices(6)
S=['001010','010001','010010','010101']
T=S+['000001']
assert set(S).issubset(V) and set(T).issubset(V)
ss=signatures(V,S); tt=signatures(V,T)
assert len(ss)==17 and all(len(x)==1 for x in ss.values())
collisions=[(sig,x) for sig,x in tt.items() if len(x)>1]
print('S',len(S),'outside',len(V)-len(S),'distinct',len(ss))
print('T',len(T),'outside',len(V)-len(T),'distinct',len(tt),'collisions:',collisions)
assert len(collisions)==1
assert collisions[0][0]==(1,2,2,3,4)
assert set(collisions[0][1])=={'001001','010100'}
print('NONMONOTONE_CERTIFICATE_PASS')
