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

    m, n = len(lines), len(lines[0])

    freq = collections.defaultdict(list)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                freq[lines[i][j]].append((i, j))

    centreNodes = {a for v in freq.values() for a in v}

    firstNodes, remainingNodes = set(), set()

    for k, v in freq.items():
        for i, a1 in enumerate(v):
            for a2 in v[i + 1 :]:
                dx = a2[0] - a1[0]
                dy = a2[1] - a1[1]

                x1, y1 = a1
                x1, y1 = x1 - dx, y1 - dy
                if x1 >= 0 and y1 >= 0 and x1 < m and y1 < n:
                    firstNodes.add((x1, y1))
                    while True:
                        x1, y1 = x1 - dx, y1 - dy
                        if x1 >= 0 and y1 >= 0 and x1 < m and y1 < n:
                            remainingNodes.add((x1, y1))
                        else:
                            break

                x2, y2 = a2
                x2, y2 = x2 + dx, y2 + dy
                if x2 >= 0 and y2 >= 0 and x2 < m and y2 < n:
                    firstNodes.add((x2, y2))
                    while True:
                        x2, y2 = x2 + dx, y2 + dy
                        if x2 >= 0 and y2 >= 0 and x2 < m and y2 < n:
                            remainingNodes.add((x2, y2))
                        else:
                            break

    ans1, ans2 = firstNodes, centreNodes.union(firstNodes).union(remainingNodes)
    ans1, ans2 = len(ans1), len(ans2)

    print(ans1, ans2)
