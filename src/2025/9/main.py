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
    # with open("./test.txt" if args.test else "./input.txt", "r") as file:
    #     lines = file.read().strip().splitlines()

    file = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
    lines = file.strip().splitlines()
    st = time.time()

    # Prepare the data here
    cords = [tuple(map(int, line.split(",")[::-1])) for line in lines]
    n = max(max(cords))

    ans1, ans2 = 0, 0

    # Logic goes here
    x_limits, y_limits = {}, {}

    for x, y in cords:
        print("x limits:")
        for c in sorted(x_limits.items()):
            print(c)

        print("y limits:")
        for c in sorted(y_limits.items()):
            print(c)

        print("\n\n")
        print("Cords:", x, y)

        print("", end="")

        if x not in y_limits and y not in x_limits:
            y_limits[x] = (y, y)
            x_limits[y] = (x, x)
        elif x not in y_limits:
            y_limits[x] = (y, y)
            t, b = x_limits[y]
            if x < t or x > b:
                for dx in range(min(b, x), max(t, x) + 1):
                    if dx in y_limits:
                        l, r = y_limits[dx]
                        if y < l or y > r:
                            l, r = min(l, y), max(r, y)
                            y_limits[dx] = (l, r)
                    else:
                        y_limits[dx] = (y, y)
                t, b = min(t, x), max(b, x)
                x_limits[y] = (t, b)
        elif y not in x_limits:
            x_limits[y] = (x, x)
            l, r = y_limits[x]
            if y < l or y > r:
                for dy in range(min(r, y), max(l, y) + 1):
                    if dy in x_limits:
                        t, b = x_limits[dy]
                        if x < t or x > b:
                            t, b = min(b, x), max(t, x)
                            x_limits[dy] = (t, b)
                    else:
                        x_limits[dy] = (x, x)
                l, r = min(l, y), max(r, y)
                y_limits[x] = (l, r)
        else:
            t, b = x_limits[y]
            l, r = y_limits[x]

            if (t <= x <= b) and (l <= y <= r):
                continue

            if x < t or x > b:
                for dx in range(min(b, x), max(t, x) + 1):
                    if dx in y_limits:
                        l, r = y_limits[dx]
                        if y < l or y > r:
                            l, r = min(l, y), max(r, y)
                            y_limits[dx] = (l, r)
                    else:
                        y_limits[dx] = (y, y)
                t, b = min(t, x), max(b, x)
                x_limits[y] = (t, b)

            l, r = y_limits[x]
            if y <= l or y >= r:
                for dy in range(l, r + 1):
                    if dy in x_limits:
                        t, b = x_limits[dy]
                        if x < t or x > b:
                            t, b = min(b, x), max(t, x)
                            x_limits[dy] = (t, b)
                    else:
                        x_limits[dy] = (x, x)
                l, r = min(l, y), max(r, y)
                y_limits[x] = (l, r)

    print("x limits:")
    for c in sorted(x_limits.items()):
        print(c)

    print("y limits:")
    for c in sorted(y_limits.items()):
        print(c)

    # for i in range(len(cords) - 1):
    #     for j in range(i + 1, len(cords)):
    #         x1, y1 = cords[i]
    #         x2, y2 = cords[j]

    #         if x1 == x2:
    #             for dy in range(min(y1, y2), max(y1, y2) + 1):
    #                 x_limits[dy] = (
    #                     min(x_limits.get(dy, (x1, x1))[0], x1, x2),
    #                     max(x_limits.get(dy, (x1, x1))[1], x1, x2),
    #                 )
    #         elif y1 == y2:
    #             for dx in range(min(x1, x2), max(x1, x2) + 1):
    #                 y_limits[dx] = (
    #                     min(y_limits.get(dx, (y1, y1))[0], y1, y2),
    #                     max(y_limits.get(dx, (y1, y1))[1], y1, y2),
    #                 )

    print("x limits:")
    for c in sorted(x_limits.items()):
        print(c)

    print("y limits:")
    for c in sorted(y_limits.items()):
        print(c)

    def check(dx, dy):
        if dy not in x_limits or dx not in y_limits:
            return False
        lx, rx = x_limits[dy]
        ty, by = y_limits[dx]
        if lx <= dx <= rx and ty <= dy <= by:
            return True

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
