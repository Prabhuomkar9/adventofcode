from collections import defaultdict
from heapq import heapify, heappop


if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()

    idx = lines.index("")

    rules = defaultdict(set)
    for line in lines[:idx]:
        l, r = line.split("|")
        rules[l].add(r)

    class Page:
        def __init__(self, val: str):
            self.val = val

        def __lt__(self, other):
            return self.val not in rules[other.val]

        def __int__(self):
            return int(self.val)

    pages = [line.split(",") for line in lines[idx + 1 :]]
    pages = [list(map(Page, page)) for page in pages]

    ans1, ans2 = 0, 0

    for page in pages:
        n = len(page)
        if all(page[i] < page[i + 1] for i in range(n - 1)):
            ans1 += int(page[n // 2])
        else:
            heapify(page)
            page = [heappop(page) for _ in range(n)]
            ans2 += int(page[n // 2])

    print(ans1, ans2)
