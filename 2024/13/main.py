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

    ans1, ans2 = 0, 0

    for i in range((len(lines) + 1) // 4):
        _, _, a1, b1 = lines[i * 4 + 0].split(" ")
        _, _, a2, b2 = lines[i * 4 + 1].split(" ")
        _, a, b = lines[i * 4 + 2].split(" ")

        a1, b1 = int(a1[2:-1]), int(b1[2:])
        a2, b2 = int(a2[2:-1]), int(b2[2:])
        a, b = int(a[2:-1]), int(b[2:])

        x = (a * b2 - b * a2) / (a1 * b2 - b1 * a2)
        y = (a * b1 - b * a1) / (a2 * b1 - b2 * a1)

        if x % 1 == 0 and y % 1 == 0:
            ans1 += 3 * x + y

        a += 10000000000000
        b += 10000000000000

        x = (a * b2 - b * a2) / (a1 * b2 - b1 * a2)
        y = (a * b1 - b * a1) / (a2 * b1 - b2 * a1)

        if x % 1 == 0 and y % 1 == 0:
            ans2 += 3 * x + y

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
