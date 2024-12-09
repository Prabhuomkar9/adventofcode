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

    matrix = list(map(lambda l: [i for i in l], lines))

    freq = collections.defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != ".":
                freq[matrix[i][j]].append((i, j))

    ans1, ans2 = set(), set()

    # TODO: logic has room for improvement

    for f in freq:
        for i in range(len(freq[f])):
            for j in range(i + 1, len(freq[f])):
                dx = freq[f][j][0] - freq[f][i][0]
                dy = freq[f][j][1] - freq[f][i][1]
                x1, y1 = freq[f][i][0] - dx, freq[f][i][1] - dy
                if x1 >= 0 and y1 >= 0 and x1 < len(matrix) and y1 < len(matrix[0]):
                    ans1.add((x1, y1))
                x2, y2 = freq[f][j][0] + dx, freq[f][j][1] + dy
                if x2 >= 0 and y2 >= 0 and x2 < len(matrix) and y2 < len(matrix[0]):
                    ans1.add((x2, y2))

    for f in freq:
        for i in range(len(freq[f])):
            for j in range(i + 1, len(freq[f])):
                dx = freq[f][j][0] - freq[f][i][0]
                dy = freq[f][j][1] - freq[f][i][1]
                x1, y1 = freq[f][i][0], freq[f][i][1]
                while True:
                    if x1 >= 0 and y1 >= 0 and x1 < len(matrix) and y1 < len(matrix[0]):
                        ans2.add((x1, y1))
                        x1, y1 = x1 - dx, y1 - dy
                    else:
                        break
                x2, y2 = freq[f][j][0], freq[f][j][1]
                while True:
                    if x2 >= 0 and y2 >= 0 and x2 < len(matrix) and y2 < len(matrix[0]):
                        ans2.add((x2, y2))
                        x2, y2 = x2 + dx, y2 + dy
                    else:
                        break

    ans1, ans2 = len(ans1), len(ans2)

    print(ans1, ans2)
