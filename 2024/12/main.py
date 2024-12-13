#!.venv/bin/python3

from argparse import ArgumentParser

import bisect
import collections
import functools
import heapq
import re
import time
import typing


if __name__ == "__main__":
    # Driver Code
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    with open("./test.txt" if args.test else "./input.txt", "r") as file:
        lines = file.read().strip().splitlines()
    st = time.time()

    m, n = len(lines), len(lines[0])

    regions = collections.defaultdict(list)
    edges = collections.defaultdict(list)
    visitedPlot = set()

    def dfs(i: int, j: int, k: int):
        visitedPlot.add((i, j))
        regions[k].append((i, j))
        for di, d in [(-1, "u"), (1, "d")]:
            di += i
            if 0 <= di < m and lines[i][j] == lines[di][j]:
                if (di, j) not in visitedPlot:
                    dfs(di, j, k)
            else:
                edges[k].append(((di + i) / 2, j, d))
        for dj, d in [(-1, "l"), (1, "r")]:
            dj += j
            if 0 <= dj < n and lines[i][j] == lines[i][dj]:
                if (i, dj) not in visitedPlot:
                    dfs(i, dj, k)
            else:
                edges[k].append((i, (dj + j) / 2, d))

    k = 0

    for i in range(m):
        for j in range(n):
            if (i, j) in visitedPlot:
                continue
            k += 1
            dfs(i, j, k)

    ans1, ans2 = 0, 0

    for r, p in regions.items():
        visitedEdge = set()
        sides = 0

        for i, j, d in edges[r]:
            if (i, j, d) in visitedEdge:
                continue
            if d in "ud":
                dj = j - 1
                while (i, dj, d) in edges[r]:
                    visitedEdge.add((i, dj, d))
                    dj -= 1
                dj = j + 1
                while (i, dj, d) in edges[r]:
                    visitedEdge.add((i, dj, d))
                    dj += 1
            else:
                di = i - 1
                while (di, j, d) in edges[r]:
                    visitedEdge.add((di, j, d))
                    di -= 1
                di = i + 1
                while (di, j, d) in edges[r]:
                    visitedEdge.add((di, j, d))
                    di += 1
            sides += 1

        ans1 += len(p) * len(edges[r])
        ans2 += len(p) * sides

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
