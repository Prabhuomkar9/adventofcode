from argparse import ArgumentParser

import bisect
import collections
import functools
import heapq
import re
import time
import typing
import math


if __name__ == "__main__":
    # Driver Code
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    with open("./test.txt" if args.test else "./input.txt", "r") as file:
        lines = file.read().strip().splitlines()
    st = time.time()

    # Prepare the data here
    cords = list(map(lambda l: list(map(int, l.split(","))), lines))

    ans1, ans2 = 0, 0

    # Logic goes here
    pq = []

    for i in range(len(cords) - 1):
        for j in range(i + 1, len(cords)):
            x1, y1, z1 = cords[i]
            x2, y2, z2 = cords[j]
            d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) ** 0.5
            pq.append((d, (x1, y1, z1), (x2, y2, z2)))

    pq.sort()

    circuits = [set() for _ in range(10 if args.test else 1000)]

    for _, c1, c2 in pq[: 10 if args.test else 1000]:
        flag = -1
        for i in range(len(circuits)):
            if flag == -1 and (
                not circuits[i] or c1 in circuits[i] or c2 in circuits[i]
            ):
                circuits[i].add(c1)
                circuits[i].add(c2)
                flag = i
            elif flag != -1 and (c1 in circuits[i] or c2 in circuits[i]):
                circuits[flag] = circuits[flag].union(circuits[i])
                circuits[i] = set()
                break

    ans1 = math.prod(sorted(map(lambda c: len(c), circuits))[-3:])

    for _, c1, c2 in pq[10 if args.test else 1000 :]:
        flag = -1
        for i in range(len(circuits)):
            if flag == -1 and (
                not circuits[i] or c1 in circuits[i] or c2 in circuits[i]
            ):
                circuits[i].add(c1)
                circuits[i].add(c2)
                flag = i
            elif flag != -1 and (c1 in circuits[i] or c2 in circuits[i]):
                circuits[flag] = circuits[flag].union(circuits[i])
                circuits[i] = set()
                break

        a = [circuit for circuit in circuits if circuit]
        if len(a) == 1 and len(a[0]) == len(cords):
            ans2 = c1[0] * c2[0]
            break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
