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

    m, n = 71, 71

    limit = 1024

    memory = [["."] * n for _ in range(m)]
    dp = [[m * n + 1] * n for _ in range(m)]

    for line in lines:
        if limit == 0:
            break
        x, y = map(int, line.split(","))
        memory[y][x] = "#"
        limit -= 1

    ans1, ans2 = 0, 0

    for m in memory:
        print("".join(m))

    stack = collections.deque()
    stack.append((0, 0, set()))

    while stack:
        x, y, seen = stack.pop()
        if dp[y][x] < len(seen):
            continue
        dp[y][x] = len(seen)
        if (x, y) == (m - 1, n - 1):
            print("here")
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx += x
            dy += y
            if (
                0 <= dx < m
                and 0 <= dy < n
                and (dx, dy) not in seen
                and memory[dy][dx] != "#"
            ):
                stack.append((dx, dy, seen.union({(x, y)})))

    ans1 += dp[m - 1][n - 1]

    # def dfs(x, y, seen):
    #     ans = float("inf")
    #     if (x, y) == (m - 1, n - 1):
    #         ans = min(ans, len(seen))
    #         return ans
    #     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #         dx += x
    #         dy += y
    #         if (
    #             0 <= dx < m
    #             and 0 <= dy < n
    #             and (dx, dy) not in seen
    #             and memory[dy][dx] != "#"
    #         ):
    #             ans = min(ans, dfs(dx, dy, seen.union({(dx, dy)})))
    #     return ans

    # ans1 += dfs(0, 0, set())

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
