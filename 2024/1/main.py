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

    left, right, freq = [], [], collections.defaultdict(int)

    for l, r in (map(int, line.split("   ")) for line in lines):
        heapq.heappush(left, l)
        heapq.heappush(right, r)
        freq[r] += 1

    ans1, ans2 = 0, 0

    for _ in range(len(lines)):
        l, r = heapq.heappop(left), heapq.heappop(right)
        ans1 += abs(l - r)
        ans2 += l * freq[l]

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
