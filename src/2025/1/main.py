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
    curr = 50

    ans1, ans2 = 0, 0

    # Logic goes here
    for line in lines:
        d, n = line[0], int(line[1:])
        q, r = divmod(n, 100)

        ans2 += q

        match d:
            case "L":
                if r >= curr and curr != 0:
                    ans2 += 1
                curr += 100 - r
                curr %= 100
            case "R":
                if r >= 100 - curr:
                    ans2 += 1
                curr += r
                curr %= 100

        if curr == 0:
            ans1 += 1

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
