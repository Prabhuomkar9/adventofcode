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

    circuits = []

    for i, (_, c1, c2) in enumerate(pq):
        insertedAt = -1

        for j in range(len(circuits)):
            if c1 in circuits[j] or c2 in circuits[j]:
                if insertedAt == -1:
                    circuits[j].update([c1, c2])
                    insertedAt = j
                else:
                    circuits[insertedAt].update(circuits[j])
                    circuits[j] = set()

        if insertedAt == -1:
            circuits.append(set([c1, c2]))

        circuits = list(filter(None, circuits))

        if i == 9 if args.test else i == 999:
            ans1 = math.prod(sorted(len(c) for c in circuits)[-3:])

        if len(circuits[0]) == len(cords):
            ans2 = c1[0] * c2[0]
            break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
