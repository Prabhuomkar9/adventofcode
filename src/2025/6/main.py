from argparse import ArgumentParser

import bisect
import collections
import functools
import heapq
import re
import time
import typing
from itertools import accumulate
import operator


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

    # Logic goes here
    j = 0

    l1 = collections.defaultdict(int)
    l2 = collections.defaultdict(int)
    op = operator.add if lines[-1][0] == "+" else operator.mul

    while True:
        flag = True

        if j < len(lines[-1]) and lines[-1][j] in "*+":
            ans1 += ([0] + list(accumulate(l1.values(), func=op)))[-1]
            ans2 += ([0] + list(accumulate(l2.values(), func=op)))[-1]

            l1.clear()
            l2.clear()
            op = operator.add if lines[-1][j] == "+" else operator.mul

        for i in range(len(lines) - 1):
            if j < len(lines[i]) and (c := lines[i][j]):
                flag = False
                if c.strip():
                    l1[i] *= 10
                    l1[i] += int(c)
                    l2[j] *= 10
                    l2[j] += int(c)

        j += 1

        if flag:
            break

    ans1 += ([0] + list(accumulate(l1.values(), func=op)))[-1]
    ans2 += ([0] + list(accumulate(l2.values(), func=op)))[-1]

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
