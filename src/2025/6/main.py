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
    groups = re.findall(r"\+\s*|\*\s*", lines[-1])

    ans1, ans2 = 0, 0

    # Logic goes here
    idx = 0
    operator.add

    for g, group in enumerate(groups):
        temp = 1 if group[0] == "*" else 0
        op = operator.mul if group[0] == "*" else operator.add

        l = collections.defaultdict(int)

        for line in lines[:-1]:
            s = line[idx : idx + len(group) if g != len(groups) - 1 else None]

            temp = op(temp, int(s))

            for i, c in enumerate(s):
                if c.strip():
                    l[i] *= 10
                    l[i] += int(c)

        ans1 += temp

        ans2 += list(accumulate(l.values(), func=op))[-1]

        idx += len(group)

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
