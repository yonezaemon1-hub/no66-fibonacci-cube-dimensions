#!/usr/bin/env python3
"""No.66 v0.3 - stand-alone full multiset verification for Gamma_9.

This code was written after the v0.2 freeze. It does not import/use the
original exhaustive search or the independent base-7 verifier. It proves
the upper bound md(Gamma_9) <= 7; the lower bound follows from the
separately certified odim(Gamma_9)=7 and odim <= md.
"""
from collections import deque
from hashlib import sha256

N = 9
LANDMARK_WORDS = (
    '010101000', '010100001', '010101010', '100101010',
    '010001001', '000100100', '010010010',
)
vertices = sorted(x for x in range(1 << N) if (x & (x >> 1)) == 0)
assert len(vertices) == 89
index = {v: i for i, v in enumerate(vertices)}
landmarks = [int(s, 2) for s in LANDMARK_WORDS]
assert len(set(landmarks)) == 7 and all(s in index for s in landmarks)
adjacency = {x: [x ^ (1 << i) for i in range(N)
                 if (x ^ (1 << i)) in index] for x in vertices}

def bfs(source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert len(dist) == 89, 'Fibonacci cube not connected'
    return dist

# Deliberately compute actual graph shortest paths, not just Hamming distances.
distance_columns = [bfs(x) for x in landmarks]
signatures = {}
for v in vertices:
    sig = tuple(sorted(col[v] for col in distance_columns))
    if sig in signatures:
        a = signatures[sig]
        raise AssertionError(f'multiset collision {a:09b} {v:09b}: {sig}')
    signatures[sig] = v
assert len(signatures) == len(vertices) == 89
assert len({tuple(sorted(col[v] for col in distance_columns))
            for v in vertices if v not in landmarks}) == 82
# The landmark signatures are also distinct from EVERY other signature.
assert len({tuple(sorted(col[x] for col in distance_columns))
            for x in landmarks}) == 7
fingerprint = sha256('\n'.join(f'{v:09b}:{tuple(sorted(col[v] for col in distance_columns))}'
                                for v in vertices).encode('ascii')).hexdigest()
print(f'NO66_GAMMA9_FULL_MULTISET_PASS vertices={len(vertices)} landmarks={len(landmarks)} '
      f'unique_signatures={len(signatures)} outside_unique=82 sha256={fingerprint}')
print('MD_GAMMA9_EXACT_7 follows from verified upper bound and frozen odim lower bound 7')
