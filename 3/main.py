import re


if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        content = file.read()

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
