#!/usr/bin/env python3
"""Portable publication wrapper; mathematical sources in src/ are unchanged."""
import argparse
import hashlib
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def verify_manifest():
    manifest = ROOT / 'SHA256SUMS.txt'
    entries = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, rel = line.split(None, 1)
        rel = rel.strip().replace('\\', '/')
        path = ROOT / rel
        require(path.resolve().is_relative_to(ROOT), 'Unsafe manifest path')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'Hash mismatch: ' + rel)
        entries.add(rel)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts} - {'SHA256SUMS.txt'}
    require(entries == actual, 'Manifest coverage differs')
    print('PUBLIC_REPRO_MANIFEST_PASS files=' + str(len(entries)), flush=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick', action='store_true', help='Omit the n=9 original k=6 and independent base-7 exhaustions; PARTIAL only')
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--compiler', default='g++')
    args = parser.parse_args()
    require(args.threads > 0, 'Threads must be positive')
    verify_manifest()
    env = dict(os.environ, OMP_NUM_THREADS=str(args.threads))
    with tempfile.TemporaryDirectory(prefix='no66_replay_') as tmp:
        build = Path(tmp)
        def run(command):
            result = subprocess.run([str(x) for x in command], cwd=ROOT, env=env,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            print(result.stdout, end='' if result.stdout.endswith('\n') else '\n', flush=True)
            require(result.returncode == 0, 'Command failed with exit ' + str(result.returncode))
            return result.stdout
        def compile_source(name, standard, extra=()):
            exe = build / (Path(name).stem + ('.exe' if os.name == 'nt' else ''))
            run([args.compiler, '-std=' + standard, '-O3', *extra, ROOT/'src'/name, '-o', exe])
            return exe
        finite = compile_source('independent_bfs_n1_to8.cpp', 'c++17')
        finite_output = run([finite])
        require('MD n=8 k=5 tested=3478761 successes=2' in finite_output, 'n=8 full multiset count')
        require('DIM n=8 k=4 tested=84280 successes=1' in finite_output, 'n=8 ordered witness')
        require('INDEPENDENT_BFS_FINITE_REPLAY_PASS' in finite_output, 'Finite replay marker')
        for name, marker in [
            ('verify_witnesses.py', 'ALL BFS WITNESS CHECKS PASS'),
            ('No66_SECONDARY_BFS_AUDIT.py', 'INDEPENDENT BFS MODEL AND BOTH NINE-DIMENSIONAL WITNESSES PASS'),
            ('verify_md_gamma9.py', 'NO66_GAMMA9_FULL_MULTISET_PASS'),
            ('verify_nonmonotonicity.py', 'NONMONOTONE_CERTIFICATE_PASS'),
        ]:
            require(marker in run([sys.executable, '-B', '-I', ROOT/'src'/name]), 'Missing marker: ' + name)
        original = compile_source('exhaustive_odim.cpp', 'c++17', ['-pthread'])
        for n, last in [(7, 4), (8, 4), (9, 5 if args.quick else 6)]:
            count_vertices = sum('11' not in format(x, '0' + str(n) + 'b') for x in range(1 << n))
            for k in range(2, last + 1):
                output = run([original, n, k, args.threads])
                match = re.search(r'EXHAUSTED n=(\d+) N=(\d+) k=(\d+) result=(\w+) tested=(\d+)', output)
                require(match is not None, 'Missing exhaustive report')
                require(match.groups() == (str(n), str(count_vertices), str(k), 'NONE', str(math.comb(count_vertices, k))), 'Exhaustive count or result mismatch')
        if not args.quick:
            base7 = compile_source('No66_INDEPENDENT_BASE7_AUDIT.cpp', 'c++20', ['-fopenmp'])
            output = run([base7])
            require('n=9 N=89 k=6 found=0 tested=581106988' in output, 'Independent base-7 mismatch')
        ordered = compile_source('No66_ORDERED_METRIC_DIMENSION_AUDIT.cpp', 'c++17')
        output = run([ordered])
        require('ORDERED_METRIC_DIM n=9 k=3 result=NONE tested=113564' in output, 'Ordered lower bound')
        require('METRIC4_FOUND' in output, 'Ordered upper witness')
    print('NO66_PUBLIC_QUICK_REPLAY_PARTIAL' if args.quick else 'NO66_PUBLIC_FULL_REPLAY_PASS')

if __name__ == '__main__':
    main()
