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

    idx = lines.index("")
    firstWarehouse = list(map(lambda l: [c for c in l], lines[:idx]))
    moves = "".join(lines[idx + 1 :])

    m, n = len(firstWarehouse), len(firstWarehouse[0])

    for i in range(m):
        for j in range(n):
            if firstWarehouse[i][j] == "@":
                x, y = i, j
                firstWarehouse[i][j] = "."

    for d in moves:
        match d:
            case "^":
                if firstWarehouse[x - 1][y] == "#":
                    continue
                if firstWarehouse[x - 1][y] == "O":
                    dx = x - 1
                    while firstWarehouse[dx][y] == "O":
                        dx -= 1
                    if firstWarehouse[dx][y] == ".":
                        firstWarehouse[dx][y] = "O"
                        firstWarehouse[x - 1][y] = "."
                if firstWarehouse[x - 1][y] == ".":
                    x -= 1
            case "v":
                if firstWarehouse[x + 1][y] == "#":
                    continue
                if firstWarehouse[x + 1][y] == "O":
                    dx = x + 1
                    while firstWarehouse[dx][y] == "O":
                        dx += 1
                    if firstWarehouse[dx][y] == ".":
                        firstWarehouse[dx][y] = "O"
                        firstWarehouse[x + 1][y] = "."
                if firstWarehouse[x + 1][y] == ".":
                    x += 1
            case "<":
                if firstWarehouse[x][y - 1] == "#":
                    continue
                if firstWarehouse[x][y - 1] == "O":
                    dy = y - 1
                    while firstWarehouse[x][dy] == "O":
                        dy -= 1
                    if firstWarehouse[x][dy] == ".":
                        firstWarehouse[x][dy] = "O"
                        firstWarehouse[x][y - 1] = "."
                if firstWarehouse[x][y - 1] == ".":
                    y -= 1
            case ">":
                if firstWarehouse[x][y + 1] == "#":
                    continue
                if firstWarehouse[x][y + 1] == "O":
                    dy = y + 1
                    while firstWarehouse[x][dy] == "O":
                        dy += 1
                    if firstWarehouse[x][dy] == ".":
                        firstWarehouse[x][dy] = "O"
                        firstWarehouse[x][y + 1] = "."
                if firstWarehouse[x][y + 1] == ".":
                    y += 1

    ans1, ans2 = 0, 0

    for i in range(m):
        for j in range(n):
            if firstWarehouse[i][j] == "O":
                ans1 += i * 100 + j

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
