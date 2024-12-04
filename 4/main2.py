if __name__ == "__main__":
    # Driver Code
    matrix = []

    with open("./input.txt", "r") as file:
        matrix = list(map(lambda x: [c for c in x], file.read().split("\n")))

    ans = 0

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "A":
                d1x, d1y = i + -1, j + -1
                d2x, d2y = i + -1, j + 1
                d3x, d3y = i + 1, j + -1
                d4x, d4y = i + 1, j + 1

                if (
                    0 <= d1x < len(matrix)
                    and 0 <= d1y < len(row)
                    and 0 <= d2x < len(matrix)
                    and 0 <= d2y < len(row)
                    and 0 <= d3x < len(matrix)
                    and 0 <= d3y < len(row)
                    and 0 <= d4x < len(matrix)
                    and 0 <= d4y < len(row)
                ):
                    if (
                        matrix[d1x][d1y] == "M"
                        and matrix[d2x][d2y] == "M"
                        and matrix[d3x][d3y] == "S"
                        and matrix[d4x][d4y] == "S"
                    ):
                        ans += 1
                    elif (
                        matrix[d1x][d1y] == "M"
                        and matrix[d2x][d2y] == "S"
                        and matrix[d3x][d3y] == "M"
                        and matrix[d4x][d4y] == "S"
                    ):
                        ans += 1
                    elif (
                        matrix[d1x][d1y] == "S"
                        and matrix[d2x][d2y] == "M"
                        and matrix[d3x][d3y] == "S"
                        and matrix[d4x][d4y] == "M"
                    ):
                        ans += 1
                    elif (
                        matrix[d1x][d1y] == "S"
                        and matrix[d2x][d2y] == "S"
                        and matrix[d3x][d3y] == "M"
                        and matrix[d4x][d4y] == "M"
                    ):
                        ans += 1

    print(ans)
