if __name__ == "__main__":
    # Driver Code
    reports = []

    with open("./input.txt", "r") as file:
        reports.extend(file.read().split("\n"))

    ans = 0

    def checkRound(levels):
        isPositive, flag = True, False

        for i in range(1, len(levels)):
            diff = levels[i] - levels[i - 1]

            if diff == 0 or abs(diff) > 3:
                flag = True
                break

            if i == 1:
                isPositive = diff > 0

            if isPositive and diff < 0:
                flag = True
                break

            if not isPositive and diff > 0:
                flag = True
                break

        return not flag

    for report in reports:
        levels = list(map(int, report.split(" ")))

        if checkRound(levels):
            ans += 1
        else:
            for i in range(len(levels)):
                newLevels = levels[:i] + levels[i + 1 :]

                if checkRound(newLevels):
                    ans += 1
                    break

    print(ans)
