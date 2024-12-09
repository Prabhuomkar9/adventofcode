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

    content = "".join(lines)

    pattern = r"^mul\(\d{1,3},\d{1,3}\)"
    dosPattern = r"^do\(\)"
    dontsPattern = r"^don't\(\)"
    allowed = True

    ans1, ans2 = 0, 0

    for i, c in enumerate(content):
        if c not in "md":
            continue
        c = content[i : i + 12]
        if m := re.search(pattern, c):
            a, b = map(int, m.group()[4:-1].split(","))
            ans1 += a * b
            if allowed:
                ans2 += a * b
        elif re.match(dosPattern, c):
            allowed = True
        elif re.match(dontsPattern, c):
            allowed = False

    print(ans1, ans2)
