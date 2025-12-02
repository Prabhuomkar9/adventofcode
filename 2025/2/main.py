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

    ans1, ans2 = 0, 0

    ranges = list(map(lambda x: x.split("-"), lines[0].split(",")))

    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            s = str(i)
            n = len(s)

            for k in range(2, n + 1):
                if n % k != 0:
                    continue

                k = n // k

                flag = True
                pat = s[:k]

                for y in range(0, len(s), k):
                    if s[y : y + k] != pat:
                        flag = False
                        break

                if flag:
                    if k == 2:
                        ans1 += int(s)
                    ans2 += int(s)
                    break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
