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

    #     file = """7,1
    # 11,1
    # 11,7
    # 9,7
    # 9,5
    # 2,5
    # 2,3
    # 7,3
    # """
    #     lines = file.strip().splitlines()
    st = time.time()

    # Prepare the data here
    cords = [tuple(map(int, line.split(",")[::-1])) for line in lines]

    n = max(cords, key=lambda x: x[1])[0]
    m = max(cords, key=lambda x: x[1])[1]

    ans1, ans2 = 0, 0

    # Logic goes here
    cx, cy = 0, 0

    for x, y in cords:
        cx += x
        cy += y

    cx /= len(cords)
    cy /= len(cords)

    n_cords = []

    for i in range(len(cords) - 1):
        for j in range(i + 1, len(cords)):
            x1, y1 = cords[i]
            x2, y2 = cords[j]
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            n_cords.append((-d, (x1, y1), (x2, y2)))

    n_cords.sort()

    seen = set()
    m_cords = []

    for _, (x1, y1), (x2, y2) in n_cords:
        if (x1, y1) not in seen:
            seen.add((x1, y1))
            m_cords.append((x1, y1))
        if (x2, y2) not in seen:
            seen.add((x2, y2))
            m_cords.append((x2, y2))

    x_limits, y_limits = {}, {}

    for i, (x, y) in enumerate(m_cords):
        print(i, len(x_limits), len(y_limits))
        x_limits_updates, y_limits_updates = set(), set()

        # print("x limits:")
        # for c in sorted(x_limits.items()):
        #     print(c)

        # print("y limits:")
        # for c in sorted(y_limits.items()):
        #     print(c)

        # print("\n\n")
        # print("Cords:", x, y)

        # print("", end="")

        if x not in y_limits and y not in x_limits:
            y_limits[x] = (y, y)
            x_limits[y] = (x, x)
        elif x not in y_limits:
            y_limits[x] = (y, y)
            t, b = x_limits[y]
            if x < t or x > b:
                y_limits_updates.update(
                    (dx, y) for dx in range(min(b, x), max(t, x) + 1)
                )
                t, b = min(t, x), max(b, x)
                x_limits[y] = (t, b)
        elif y not in x_limits:
            x_limits[y] = (x, x)
            l, r = y_limits[x]
            if y < l or y > r:
                x_limits_updates.update(
                    (x, dy) for dy in range(min(r, y), max(l, y) + 1)
                )
                l, r = min(l, y), max(r, y)
                y_limits[x] = (l, r)
        else:
            t, b = x_limits[y]
            l, r = y_limits[x]

            if (t <= x <= b) and (l <= y <= r):
                continue

            if x < t or x > b:
                y_limits_updates.update(
                    (dx, y) for dx in range(min(b, x), max(t, x) + 1)
                )
                t, b = min(t, x), max(b, x)
                x_limits[y] = (t, b)

            if y < l or y > r:
                x_limits_updates.update(
                    (x, dy) for dy in range(min(r, y), max(l, y) + 1)
                )
                l, r = min(l, y), max(r, y)
                y_limits[x] = (l, r)

        while x_limits_updates:
            x, dy = x_limits_updates.pop()
            if dy in x_limits:
                t, b = x_limits[dy]
                if x < t or x > b:
                    y_limits_updates.update(
                        (dx, dy) for dx in range(min(b, x), max(t, x) + 1)
                    )
                    t, b = min(t, x), max(b, x)
                    x_limits[dy] = (t, b)
            else:
                x_limits[dy] = (x, x)

        while y_limits_updates:
            dx, y = y_limits_updates.pop()
            if dx in y_limits:
                l, r = y_limits[dx]
                if y < l or y > r:
                    x_limits_updates.update(
                        (dx, dy) for dy in range(min(r, y), max(l, y) + 1)
                    )
                    l, r = min(l, y), max(r, y)
                    y_limits[dx] = (l, r)
            else:
                y_limits[dx] = (y, y)

        while x_limits_updates:
            x, dy = x_limits_updates.pop()
            if dy in x_limits:
                t, b = x_limits[dy]
                if x < t or x > b:
                    t, b = min(b, x), max(t, x)
                    x_limits[dy] = (t, b)
            else:
                x_limits[dy] = (x, x)

    # print("\n\n")
    # print("Final")

    # print("x limits:")
    # for c in sorted(x_limits.items()):
    #     print(c)

    # print("y limits:")
    # for c in sorted(y_limits.items()):
    #     print(c)

    def check(dx, dy):
        if dy not in x_limits or dx not in y_limits:
            return False
        lx, rx = x_limits[dy]
        ty, by = y_limits[dx]
        if lx <= dx <= rx and ty <= dy <= by:
            return True

    # print("here")
    # with open("out.txt", "w") as f:
    #     f.write("")

    # with open("out.txt", "a") as f:
    #     for i in range(n + 1):
    #         c = ""
    #         for j in range(n + 1):
    #             c += "X" if check(i, j) else "."
    #         c += "\n"
    #         f.write(c)

    for i in range(len(cords) - 1):
        for j in range(i + 1, len(cords)):
            x1, y1 = cords[i]
            x2, y2 = cords[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            ans1 = max(ans1, area)

            if check(x1, y2) and check(x2, y1):
                ans2 = max(ans2, area)

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
