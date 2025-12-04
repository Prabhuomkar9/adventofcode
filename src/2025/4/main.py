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
    matrix = [[c for c in line] for line in lines]

    ans1, ans2 = 0, 0

    # Logic goes here
    flag = False

    while True:
        flag2 = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == ".":
                    continue

                c = 0
                for x, y in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]:
                    di = i + x
                    dj = j + y
                    if 0 <= di < len(matrix) and 0 <= dj < len(matrix[0]):
                        if matrix[di][dj] in ["@", "X"]:
                            c += 1

                if c < 4:
                    matrix[i][j] = "X"
                    if not flag:
                        ans1 += 1
                    ans2 += 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "X":
                    matrix[i][j] = "."
                    flag2 = False

        flag = True

        if flag2:
            break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
