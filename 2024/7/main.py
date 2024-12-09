from argparse import ArgumentParser

import bisect
import collections
import heapq
import re


if __name__ == "__main__":
    # Driver Code
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    with open("./test.txt" if args.test else "./input.txt", "r") as file:
        lines = file.read().strip().splitlines()

    equation = list(map(lambda l: l.split(), lines))

    ans1, ans2 = 0, 0

    # TODO: logic has room for improvement
    for res, *a in equation:
        res = int(res[:-1])
        a = list(map(int, a))

        def dfs(i, cRes, op):
            if cRes > res:
                return 0

            if i == len(a):
                return res if cRes == res else 0

            nRes = cRes + a[i] if op == "+" else cRes * a[i]

            l = dfs(i + 1, nRes, "+")
            if l > 0:
                return l
            else:
                return dfs(i + 1, nRes, "*")

        l = dfs(1, a[0], "+")
        if l > 0:
            ans1 += l
        else:
            ans1 += dfs(1, a[0], "*")

    for res, *a in equation:
        res = int(res[:-1])
        a = list(map(int, a))

        def dfs(i, cRes, op):
            if cRes > res:
                return 0

            if i == len(a):
                return res if cRes == res else 0

            nRes = (
                cRes + a[i]
                if op == "+"
                else cRes * a[i] if op == "*" else int(f"{cRes}{a[i]}")
            )

            l = dfs(i + 1, nRes, "+")
            if l > 0:
                return l
            else:
                r = dfs(i + 1, nRes, "*")
                if r > 0:
                    return r
                else:
                    return dfs(i + 1, nRes, "|")

        l = dfs(1, a[0], "+")
        if l > 0:
            ans2 += l
        else:
            r = dfs(1, a[0], "*")
            if r > 0:
                ans2 += r
            else:
                ans2 += dfs(1, a[0], "|")

    print(ans1, ans2)
