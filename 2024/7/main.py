from argparse import ArgumentParser

import functools
import bisect
import collections
import heapq
import re
import typing


if __name__ == "__main__":
    # Driver Code
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    with open("./test.txt" if args.test else "./input.txt", "r") as file:
        lines = file.read().strip().splitlines()

    ans1, ans2 = 0, 0

    # TODO: logic has room for improvement, bottom up
    for res, *a in [l.split() for l in lines]:
        res = int(res[:-1])
        a = list(map(int, a))

        @functools.lru_cache(None)
        def dfs(i: int, cRes: int, op: typing.Literal["+", "*", "|"], res: int):
            if cRes > res:
                return (0, 0)

            if i == len(a):
                return (res, res) if cRes == res else (0, 0)

            match op:
                case "+":
                    nRes = cRes + a[i]
                case "*":
                    nRes = cRes * a[i]
                case "|":
                    nRes = int(f"{cRes}{a[i]}")

            l, r = dfs(i + 1, nRes, "+", res)

            if l <= 0:
                l, _ = dfs(i + 1, nRes, "*", res)

            if r <= 0:
                _, r = dfs(i + 1, nRes, "*", res)
                if r <= 0:
                    _, r = dfs(i + 1, nRes, "|", res)

            return l, r

        l, r = dfs(1, a[0], "+", res)

        if l <= 0:
            l, _ = dfs(1, a[0], "*", res)

        if r <= 0:
            _, r = dfs(1, a[0], "*", res)
            if r <= 0:
                _, r = dfs(1, a[0], "|", res)

        ans1 += l
        ans2 += r

    print(ans1, ans2)
