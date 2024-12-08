from collections import defaultdict

if __name__ == "__main__":
    # Driver Code
    matrix = []

    with open("./input.txt", "r") as file:
        matrix = list(map(lambda l: [i for i in l], file.read().splitlines()))

    freq = defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != ".":
                freq[matrix[i][j]].append((i, j))

    ans = set()

    for f in freq:
        for i in range(len(freq[f])):
            for j in range(i + 1, len(freq[f])):
                dx = freq[f][j][0] - freq[f][i][0]
                dy = freq[f][j][1] - freq[f][i][1]
                x1, y1 = freq[f][i][0] - dx, freq[f][i][1] - dy
                if x1 >= 0 and y1 >= 0 and x1 < len(matrix) and y1 < len(matrix[0]):
                    ans.add((x1, y1))
                x2, y2 = freq[f][j][0] + dx, freq[f][j][1] + dy
                if x2 >= 0 and y2 >= 0 and x2 < len(matrix) and y2 < len(matrix[0]):
                    ans.add((x2, y2))

    print(len(ans))
