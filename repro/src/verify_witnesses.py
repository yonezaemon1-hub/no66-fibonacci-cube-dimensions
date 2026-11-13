#!/usr/bin/env python3
"""Independent BFS-based witness audit for Fibonacci cubes (standard library only)."""
from collections import deque
from itertools import combinations

WITNESSES = {
    1: ['0'],
    2: ['01'],
    3: ['001', '010'],
    4: ['0001', '0010', '0101'],
    5: ['00101', '01001', '10101'],
    6: ['001010', '010001', '010010', '010101'],
    7: ['0000010', '0010010', '0010100', '1001010', '1010101'],
    8: ['01001010', '01010001', '01010010', '01010101', '10010101'],
    9: ['010101000', '010100001', '010101010', '100101010', '010001001', '000100100', '010010010'],
    10: ['1000100101', '0100101010', '0001001010', '0101000010', '1001001001', '0101010101', '0100101001'],
    11: ['00001001001', '10000001001', '00100101001', '10010101001', '10101010101', '01010100101', '01000010101', '10100001001', '10010000001'],
}


def vertices(n):
    return [s for x in range(1 << n)
            if '11' not in (s := format(x, f'0{n}b'))]


def distances_from(source, adjacency):
    d = {source: 0}
    q = deque([source])
    while q:
        v = q.popleft()
        for w in adjacency[v]:
            if w not in d:
                d[w] = d[v] + 1
                q.append(w)
    return d


def audit(n, landmarks):
    vs = vertices(n)
    vset = set(vs)
    assert len(landmarks) == len(set(landmarks)) and set(landmarks) <= vset
    adj = {v: [] for v in vs}
    for v in vs:
        for i in range(n):
            w = v[:i] + ('1' if v[i] == '0' else '0') + v[i + 1:]
            if w in vset:
                adj[v].append(w)
    d = {w: distances_from(w, adj) for w in landmarks}
    for u in vs:
        for w in landmarks:
            # This isometric property is independently checked for all used witnesses.
            assert d[w][u] == sum(x != y for x, y in zip(u, w)), (n, u, w)
    signatures = {}
    for u in vs:
        if u in landmarks:
            continue
        key = tuple(sorted(d[w][u] for w in landmarks))
        assert key not in signatures, (n, u, signatures.get(key), key)
        signatures[key] = u
    print(f'WITNESS PASS n={n} vertices={len(vs)} landmarks={len(landmarks)} external={len(signatures)}')


def audit_small_lower():
    # Fully independent enumeration for small dimensions, to catch any encoding bug.
    for n, minimum in [(1,1), (2,1), (3,2), (4,3), (5,3), (6,4)]:
        vs = vertices(n)
        graph = {v:[w for w in vs if sum(x != y for x,y in zip(v,w)) == 1] for v in vs}
        d = {v: distances_from(v, graph) for v in vs}
        for k in range(minimum):
            for ss in combinations(vs,k):
                fingerprints = [tuple(sorted(d[w][v] for w in ss)) for v in vs if v not in ss]
                assert len(fingerprints) != len(set(fingerprints)), (n,k,ss)
        print(f'INDEPENDENT LOWER PASS n={n} exact_minimum={minimum}')

if __name__ == '__main__':
    audit_small_lower()
    for n, ws in WITNESSES.items():
        audit(n, ws)
    print('ALL BFS WITNESS CHECKS PASS; lower bounds for n=7,8,9 require C++ exhaustive check.')
