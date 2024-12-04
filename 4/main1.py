if __name__ == "__main__":
    # Driver Code
    matrix = []

    with open("./input.txt", "r") as file:
        matrix = list(map(lambda x: [c for c in x], file.read().split("\n")))

    ans = 0

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "X":
                possible = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]

                for c in ["M", "A", "S"]:
                    newPossible = []
                    for dx, dy in possible:
                        x = i + dx
                        y = j + dy

                        if x >= 0 and x < len(matrix) and y >= 0 and y < len(row):
                            if matrix[x][y] == c:
                                if c == "S":
                                    ans += 1
                                newPossible.append(
                                    (
                                        dx + (1 if dx > 0 else -1 if dx < 0 else 0),
                                        dy + (1 if dy > 0 else -1 if dy < 0 else 0),
                                    )
                                )
                    possible = newPossible

    print(ans)
