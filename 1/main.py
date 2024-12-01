if __name__ == "__main__":
    # Driver Code
    left, right = [], []
    rows = []

    with open("./input.txt", "r") as file:
        rows.extend(file.read().split("\n"))

    for row in rows:
        l, r = row.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    ans = 0

    for l, r in zip(left, right):
        print(l, r)
        ans += abs(l - r)

    print(ans)
