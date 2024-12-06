if __name__ == "__main__":
    # Driver Code
    matrix = []
    idx = (0, 0)

    with open("./input.txt", "r") as file:
        lines = file.read().split()
        for i, line in enumerate(lines):
            matrix.append([x for x in line])
            if "^" in line:
                idx = (i, line.index("^"))
                matrix[idx[0]][idx[1]] = "X"

    direction = "u"

    while True:
        match direction:
            case "u":
                if idx[0] - 1 < 0:
                    break
                if matrix[idx[0] - 1][idx[1]] == "#":
                    direction = "r"
                    idx = (idx[0], idx[1] + 1)
                else:
                    idx = (idx[0] - 1, idx[1])
            case "r":
                if idx[1] + 1 >= len(matrix[0]):
                    break
                if matrix[idx[0]][idx[1] + 1] == "#":
                    direction = "d"
                    idx = (idx[0] + 1, idx[1])
                else:
                    idx = (idx[0], idx[1] + 1)
            case "d":
                if idx[0] + 1 >= len(matrix):
                    break
                if matrix[idx[0] + 1][idx[1]] == "#":
                    direction = "l"
                    idx = (idx[0], idx[1] - 1)
                else:
                    idx = (idx[0] + 1, idx[1])
            case "l":
                if idx[1] - 1 < 0:
                    break
                if matrix[idx[0]][idx[1] - 1] == "#":
                    direction = "u"
                    idx = (idx[0] - 1, idx[1])
                else:
                    idx = (idx[0], idx[1] - 1)

        matrix[idx[0]][idx[1]] = "X"

    print(sum(line.count("X") for line in matrix))
