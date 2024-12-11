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

    idx = lines.index("")

    rules = collections.defaultdict(set)
    for line in lines[:idx]:
        l, r = line.split("|")
        rules[l].add(r)

    class Page:
        def __init__(self, val: str):
            self.val = val

        def __lt__(self, other):
            return self.val not in rules[other.val]

        def __int__(self):
            return int(self.val)

    pages = [line.split(",") for line in lines[idx + 1 :]]
    pages = [list(map(Page, page)) for page in pages]

    ans1, ans2 = 0, 0

    for page in pages:
        n = len(page)
        if all(page[i] < page[i + 1] for i in range(n - 1)):
            ans1 += int(page[n // 2])
        else:
            heapq.heapify(page)
            page = [heapq.heappop(page) for _ in range(n)]
            ans2 += int(page[n // 2])

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
