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

    reports = [list(map(int, line.split(" "))) for line in lines]

    ans1, ans2 = 0, 0

    for report in reports:
        diff = [report[i] - report[i - 1] for i in range(1, len(report))]
        sign = 1 if diff[0] > 0 else -1

        if all(abs(d) <= 3 and sign * d > 0 for d in diff):
            ans1 += 1
            ans2 += 1
        else:
            for i, r in enumerate(report):
                report = report[:i] + report[i + 1 :]

                diff = [report[i] - report[i - 1] for i in range(1, len(report))]
                sign = 1 if diff[0] > 0 else -1

                report = report[:i] + [r] + report[i:]

                if all(abs(d) <= 3 and sign * d > 0 for d in diff):
                    ans2 += 1
                    break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
