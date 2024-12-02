from collections import defaultdict

if __name__ == "__main__":
    # Driver Code
    left, right = defaultdict(int), defaultdict(int)
    rows = []

    with open("./input.txt", "r") as file:
        rows.extend(file.read().split("\n"))

    for row in rows:
        l, r = row.split("   ")
        left[int(l)] += 1
        right[int(r)] += 1

    ans = 0

    for n, l in left.items():
        ans += n * l * right[n]

    print(ans)
