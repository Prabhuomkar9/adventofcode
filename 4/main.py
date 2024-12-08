if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()

    m, n = len(lines), len(lines[0])

    centres = []

    for i in range(m):
        for j in range(n):
            if lines[i][j] == "A":
                centres.append((i, j))

    ans1, ans2 = 0, 0

    for i, j in centres:
        if 0 < i < m - 1:
            ttb = lines[i - 1][j] + lines[i + 1][j]
            if ttb == "MS":
                ans1 += i - 2 >= 0 and lines[i - 2][j] == "X"
            elif ttb == "SM":
                ans1 += i + 2 < m and lines[i + 2][j] == "X"

        if 0 < j < n - 1:
            ltr = lines[i][j - 1] + lines[i][j + 1]
            if ltr == "MS":
                ans1 += j - 2 >= 0 and lines[i][j - 2] == "X"
            elif ltr == "SM":
                ans1 += j + 2 < n and lines[i][j + 2] == "X"

        if 0 < i < m - 1 and 0 < j < n - 1:
            lttrb = lines[i - 1][j - 1] + lines[i + 1][j + 1]
            if lttrb == "MS":
                ans1 += i - 2 >= 0 and j - 2 >= 0 and lines[i - 2][j - 2] == "X"
            elif lttrb == "SM":
                ans1 += i + 2 < m and j + 2 < n and lines[i + 2][j + 2] == "X"

            lbtrt = lines[i - 1][j + 1] + lines[i + 1][j - 1]
            if lbtrt == "MS":
                ans1 += i - 2 >= 0 and j + 2 < n and lines[i - 2][j + 2] == "X"
            elif lbtrt == "SM":
                ans1 += i + 2 < m and j - 2 >= 0 and lines[i + 2][j - 2] == "X"

            if lttrb in ["MS", "SM"] and lbtrt in ["MS", "SM"]:
                ans2 += 1

    print(ans1, ans2)