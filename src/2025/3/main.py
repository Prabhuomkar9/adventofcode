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
    banks = [[int(x) for x in line] for line in lines]

    ans1, ans2 = 0, 0

    # Logic goes here
    for bank in banks:
        n = len(bank)

        battery = []

        idx = -1
        curr = -1

        for j in range(2):
            for i in range(idx + 1, n - 1 + j):
                if bank[i] > curr:
                    idx, curr = i, bank[i]

            battery.append(f"{curr}")
            idx += 1
            curr = bank[idx] if idx < n else 0

        ans1 += int("".join(battery))

        battery = []

        idx = -1
        curr = -1

        for j in range(12):
            for i in range(idx + 1, n - 11 + j):
                if bank[i] > curr:
                    idx, curr = i, bank[i]

            battery.append(f"{curr}")
            idx += 1
            curr = bank[idx] if idx < n else 0

        ans2 += int("".join(battery))

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
