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

    w, h, sec = 101, 103, 100

    positions = collections.defaultdict(int)

    for l in lines:
        p, v = l.split(" ")
        p = tuple(map(int, p[2:].split(",")))
        v = tuple(map(int, v[2:].split(",")))
        x = (p[0] + v[0] * sec) % w
        y = (p[1] + v[1] * sec) % h
        positions[(y, x)] += 1

    ans1, ans2 = 0, 0

    tl, tr, bl, br = 0, 0, 0, 0

    for i in range(h):
        for j in range(w):
            if i == h // 2 or j == w // 2:
                continue

            if i < h // 2:
                if j < w // 2:
                    tl += positions[(i, j)]
                else:
                    tr += positions[(i, j)]
            else:
                if j < w // 2:
                    bl += positions[(i, j)]
                else:
                    br += positions[(i, j)]

    ans1 = tl * tr * bl * br

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
