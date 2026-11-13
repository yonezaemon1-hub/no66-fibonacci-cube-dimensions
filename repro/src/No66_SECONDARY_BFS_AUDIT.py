#!/usr/bin/env python3
"""Independent graph-distance audit, no imports from the No.66 candidate."""
from collections import deque


def graph(n):
    v = [x for x in range(1 << n) if not (x & (x << 1))]
    allowed = set(v)
    neighbors = {x: [y for bit in range(n)
                     if (y := x ^ (1 << bit)) in allowed] for x in v}
    return v, neighbors


def bfs(start, neighbors):
    distance = {start: 0}
    frontier = deque([start])
    while frontier:
        v = frontier.popleft()
        for w in neighbors[v]:
            if w not in distance:
                distance[w] = distance[v] + 1
                frontier.append(w)
    return distance


def isometry(n):
    vs, neighbors = graph(n)
    for w in vs:
        dist = bfs(w, neighbors)
        assert len(dist) == len(vs)
        for v in vs:
            assert dist[v] == (w ^ v).bit_count(), (n, w, v)
    print(f'ISOMETRY_PASS n={n} vertices={len(vs)} ordered_pairs={len(vs)**2}')


def check_landmarks(n, names, unordered):
    vs, adj = graph(n)
    landmarks = [int(x, 2) for x in names]
    assert len(landmarks) == len(set(landmarks))
    assert set(landmarks).issubset(vs)
    data = [bfs(s, adj) for s in landmarks]
    outside = [v for v in vs if v not in landmarks] if unordered else vs
    sigs = [tuple(sorted(dist[v] for dist in data)) if unordered
            else tuple(dist[v] for dist in data) for v in outside]
    assert len(sigs) == len(set(sigs)), (n, len(names), unordered)
    print(f'{"OUTER" if unordered else "ORDERED"}_PASS n={n} '
          f'landmarks={len(names)} resolved={len(outside)}')


if __name__ == '__main__':
    for n in range(1, 10):
        isometry(n)
    check_landmarks(9, [
        '010101000', '010100001', '010101010',
        '100101010', '010001001', '000100100', '010010010',
    ], True)
    check_landmarks(9, [
        '000101001', '010010101', '100100101', '101010001',
    ], False)
    print('INDEPENDENT BFS MODEL AND BOTH NINE-DIMENSIONAL WITNESSES PASS')
