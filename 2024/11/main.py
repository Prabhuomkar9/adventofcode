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

    stones = collections.defaultdict(int)

    for stone in lines[0].split(" "):
        stones[stone] += 1

    ans1, ans2 = 0, 0

    for i in range(75):
        f = stones.copy()
        for k, v in f.items():
            stones[k] -= v

            if len(k) % 2 == 0:
                l = k[: len(k) // 2].lstrip("0")
                r = k[len(k) // 2 :].lstrip("0")
                stones[l if l else "0"] += v
                stones[r if r else "0"] += v
            else:
                stones[f"{max(1, int(k)*2024)}"] += v

        if i == 24:
            ans1 += sum([v for v in stones.values() if v != 0])

    ans2 += sum([v for v in stones.values() if v != 0])

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
