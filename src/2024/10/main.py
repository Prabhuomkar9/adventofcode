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

    direction = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}

    trails = collections.defaultdict(set)

    for i in range(m):
        for j in range(n):
            stack = collections.deque()
            stack.append((i, j, 0, ""))

            while stack:
                ci, cj, h, movement = stack.pop()

                if lines[ci][cj] != f"{h}":
                    continue

                if h == 9:
                    trails[(i, j)].add((movement, (ci, cj)))
                    trails[(ci, cj)].add((i, j))
                    continue

                for d, (di, dj) in direction.items():
                    di, dj = ci + di, cj + dj
                    if 0 <= di < m and 0 <= dj < n:
                        stack.append((di, dj, h + 1, movement + d))

    ans1, ans2 = 0, 0

    for i in range(m):
        for j in range(n):
            if lines[i][j] == "9":
                ans1 += len(trails[(i, j)])
            if lines[i][j] == "0":
                ans2 += len(trails[(i, j)])

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
