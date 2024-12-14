#!.venv/bin/python3

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

    w, h, sec = 101, 103, 100

    positions = collections.defaultdict(int)
    robots = []

    class Robot:
        def __init__(self, x: int, y: int, vx: int, vy: int) -> None:
            self.x = x
            self.y = y
            self.vx = vx
            self.vy = vy

        def move(self):
            self.x = (self.x + self.vx) % w
            self.y = (self.y + self.vy) % h

    for l in lines:
        p, v = l.split(" ")
        p = tuple(map(int, p[2:].split(",")))
        v = tuple(map(int, v[2:].split(",")))
        robots.append(Robot(p[0], p[1], v[0], v[1]))
        x = (p[0] + v[0] * sec) % w
        y = (p[1] + v[1] * sec) % h
        positions[(y, x)] += 1

    ans1, ans2 = 0, 0

    tl, tr, bl, br = 0, 0, 0, 0

    for (i, j), c in positions.items():
        if i == h // 2 or j == w // 2:
            continue

        if i < h // 2:
            if j < w // 2:
                tl += positions[(i, j)]
            else:
                tr += positions[(i, j)]
        else:
            if j < w // 2:
                bl += positions[(i, j)]
            else:
                br += positions[(i, j)]

    ans1 = tl * tr * bl * br

    i = 0

    while True:
        i += 1

        # TODO: use statistical methods to find cluster of tree
        s = set()
        for robot in robots:
            robot.move()
            s.add((robot.x, robot.y))

        if len(s) == len(robots):
            grid = [["."] * w for _ in range(h)]
            for robot in robots:
                grid[robot.y][robot.x] = "X"
            for line in grid:
                print("".join(map(str, line)))
            correct = input(f"[y/N]: ")
            if correct == "y":
                ans2 = i
                break

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
