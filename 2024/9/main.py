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

    # TODO: logic has room for improvement
    content = lines[0]

    fileSystem, i, isBlock = [], 0, True
    emptyBlocks = []
    fileBlocks = []

    for c in content:
        if isBlock:
            fileBlocks.append((len(fileSystem), int(c)))
            fileSystem.extend([i] * int(c))
            i += 1
        else:
            emptyBlocks.append((len(fileSystem), int(c)))
            fileSystem.extend(["."] * int(c))
        isBlock = not isBlock

    i, j = 0, len(fileSystem) - 1
    ans1FileSystem = fileSystem.copy()

    while i < j:
        while ans1FileSystem[i] != ".":
            i += 1
        while ans1FileSystem[j] == ".":
            j -= 1
        if i < j:
            ans1FileSystem[i], ans1FileSystem[j] = ans1FileSystem[j], ans1FileSystem[i]
            i += 1
            j -= 1

    ans2FileSystem = fileSystem.copy()

    for f in reversed(fileBlocks):
        i = bisect.bisect(emptyBlocks, f)
        for i, e in enumerate(emptyBlocks[:i]):
            if e[1] >= f[1]:
                (
                    ans2FileSystem[e[0] : e[0] + f[1]],
                    ans2FileSystem[f[0] : f[0] + f[1]],
                ) = (
                    ans2FileSystem[f[0] : f[0] + f[1]],
                    ans2FileSystem[e[0] : e[0] + f[1]],
                )
                emptyBlocks[i] = (e[0], 0)
                emptyBlocks.insert(i + 1, (e[0] + f[1], e[1] - f[1]))
                break

    ans1, ans2 = 0, 0

    for i, c in enumerate(ans1FileSystem):
        if c == ".":
            break
        else:
            ans1 += i * int(c)

    for i, c in enumerate(ans2FileSystem):
        if c == ".":
            continue
        else:
            ans2 += i * int(c)

    print(ans1, ans2)
