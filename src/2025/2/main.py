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
    ranges = list(map(lambda x: list(map(int, x.split("-"))), lines[0].split(",")))

    ans1, ans2 = 0, 0

    # Logic goes here
    for r in ranges:
        for num in range(r[0], r[1] + 1):
            s = str(num)
            n = len(s)

            for k in range(2, n + 1):
                if n % k != 0:
                    continue

                pat_len = n // k

                pat = s[:pat_len]

                for y in range(0, n, pat_len):
                    if s[y : y + pat_len] != pat:
                        break
                else:
                    if k == 2:
                        ans1 += int(s)
                    ans2 += int(s)
                    break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
