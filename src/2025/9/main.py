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
    cords = [tuple(map(int, line.split(",")[::-1])) for line in lines]
    n = max(max(cords))

    ans1, ans2 = 0, 0

    # Logic goes here
    x_limits, y_limits = {}, {}

    def check(dx, dy):
        if dy not in x_limits or dx not in y_limits:
            return False
        lx, rx = x_limits[dy]
        ty, by = y_limits[dx]
        if lx <= dx <= rx and ty <= dy <= by:
            return True

    for i in range(len(cords) - 1):
        for j in range(i + 1, len(cords)):
            x1, y1 = cords[i]
            x2, y2 = cords[j]

            if x1 == x2:
                for dy in range(min(y1, y2), max(y1, y2) + 1):
                    x_limits[dy] = (
                        min(x_limits.get(dy, (x1, x1))[0], x1, x2),
                        max(x_limits.get(dy, (x1, x1))[1], x1, x2),
                    )
            elif y1 == y2:
                for dx in range(min(x1, x2), max(x1, x2) + 1):
                    y_limits[dx] = (
                        min(y_limits.get(dx, (y1, y1))[0], y1, y2),
                        max(y_limits.get(dx, (y1, y1))[1], y1, y2),
                    )

    print("here")
    with open("out.txt", "w") as f:
        f.write("")

    with open("out.txt", "a") as f:
        for i in range(n + 1):
            c = ""
            for j in range(n + 1):
                c += "X" if check(i, j) else "."
            c += "\n"
            f.write(c)

    for i in range(len(cords) - 1):
        for j in range(i + 1, len(cords)):
            x1, y1 = cords[i]
            x2, y2 = cords[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            ans1 = max(ans1, area)

            if check(x1, y1) and check(x2, y2) and check(x1, y2) and check(x2, y1):
                ans2 = max(ans2, area)

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
