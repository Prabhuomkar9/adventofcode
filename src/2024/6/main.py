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

    for i, line in enumerate(lines):
        if "^" in line:
            idx = (i, line.index("^"))

    m, n = len(lines), len(lines[0])

    iChanges = {"u": (-1, 0), "r": (0, 1), "d": (1, 0), "l": (0, -1)}
    dChanges = {"u": "r", "r": "d", "d": "l", "l": "u"}

    ans1, ans2 = 0, 0

    currIdx = idx
    direction = "u"
    seen = set({currIdx})

    while True:
        dx, dy = iChanges[direction]
        dx, dy = dx + currIdx[0], dy + currIdx[1]

        if not (0 <= dx < m and 0 <= dy < n):
            ans1 += len(seen)
            break

        if lines[dx][dy] == "#":
            direction = dChanges[direction]
        else:
            currIdx = (dx, dy)

        seen.add(currIdx)

    seen.remove(idx)

    for i, j in seen:
        currIdx = idx
        direction = "u"
        seen = set()

        while True:
            dx, dy = iChanges[direction]
            dx, dy = dx + currIdx[0], dy + currIdx[1]

            if not (0 <= dx < m and 0 <= dy < n):
                break

            if lines[dx][dy] == "#" or (dx, dy) == (i, j):
                direction = dChanges[direction]
            else:
                currIdx = (dx, dy)

            if (currIdx, direction) in seen:
                ans2 += 1
                break

            seen.add((currIdx, direction))

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
