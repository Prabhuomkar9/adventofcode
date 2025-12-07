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

    # Prepare the data here
    mat = [[c for c in line] for line in lines]
    n, m = len(mat), len(mat[0])

    ans1, ans2 = 0, 0

    # Logic goes here
    dp = [0] * m
    dp[mat[0].index("S")] = 1

    for i in range(n - 1):
        new_dp = [0] * m
        for j in range(m):
            if mat[i + 1][j] == "^":
                ans1 += 1
                for dj in [-1, 1]:
                    if 0 <= j + dj < n:
                        new_dp[j + dj] += dp[j]
            else:
                new_dp[j] += dp[j]
        dp = new_dp

    ans2 = sum(dp)

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
