if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        content = file.read()

    fileSystem, i, isBlock = [], 0, True

    for c in content:
        if isBlock:
            fileSystem.extend([i] * int(c))
            i += 1
        else:
            fileSystem.extend(["."] * int(c))
        isBlock = not isBlock

    i, j = 0, len(fileSystem) - 1

    while i < j:
        while fileSystem[i] != ".":
            i += 1
        while fileSystem[j] == ".":
            j -= 1
        if i < j:
            fileSystem[i], fileSystem[j] = fileSystem[j], fileSystem[i]
            i += 1
            j -= 1

    ans1, ans2 = 0, 0

    for i, c in enumerate(fileSystem):
        if c == ".":
            break
        else:
            ans1 += i * int(c)

    print(ans1, ans2)
