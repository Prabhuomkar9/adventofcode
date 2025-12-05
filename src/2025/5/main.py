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
    idx = lines.index("")
    ranges = [list(map(int, line.split("-"))) for line in lines[:idx]]
    elements = [int(line) for line in lines[idx + 1 :]]

    ans1, ans2 = 0, 0

    # Logic goes here
    ranges.sort()

    merged_ranges = [ranges[0]]

    ans2 += merged_ranges[0][1] - merged_ranges[0][0] + 1

    for l, r in ranges[1:]:
        if l <= merged_ranges[-1][1] < r:
            ans2 += r - merged_ranges[-1][1]
            merged_ranges[-1][1] = r
        else:
            ans2 += r - l + 1
            merged_ranges.append([l, r])

    for element in elements:
        idx = bisect.bisect_left(merged_ranges, element, key=lambda x: x[0])
        if 0 <= idx < len(merged_ranges) and element == merged_ranges[idx][0]:
            ans1 += 1
        elif 0 <= idx - 1:
            if element <= merged_ranges[idx - 1][1]:
                ans1 += 1

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
