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

    a = int(lines[0].split(": ")[1])
    prg = list(map(int, lines[4].split(": ")[1].split(",")))

    ans1, ans2 = 0, 0

    out1 = []

    for da in range(1000):
        og_da = da
        combo = lambda x: x if x <= 3 else da if x == 4 else b if x == 5 else c

        b = int(lines[1].split(": ")[1])
        c = int(lines[2].split(": ")[1])

        i, out2 = 0, []

        while i < len(prg) - 1:
            opcode = prg[i]
            operand = prg[i + 1]

            match opcode:
                case 0:
                    da //= 2 ** combo(operand)
                case 1:
                    b ^= operand
                case 2:
                    b = combo(operand) % 8
                case 3:
                    if da != 0:
                        i = operand
                        continue
                case 4:
                    b ^= c
                case 5:
                    out2.append(combo(operand) % 8)
                case 6:
                    b = da // (2 ** combo(operand))
                case 7:
                    c = da // (2 ** combo(operand))
                case _:
                    pass

            i += 2

        if og_da == a:
            out1 = out2.copy()

        if out2 == prg:
            print("Hello world")
            print(da)
            break

    ans1 = ",".join(map(str, out1))

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
