from heapq import heappush, heappop
from collections import defaultdict


if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()

    left, right, freq = [], [], defaultdict(int)

    for l, r in (map(int, line.split("   ")) for line in lines):
        heappush(left, l)
        heappush(right, r)
        freq[r] += 1

    ans1, ans2 = 0, 0

    for _ in range(len(lines)):
        l, r = heappop(left), heappop(right)
        ans1 += abs(l - r)
        ans2 += l * freq[l]

    print(ans1, ans2)
