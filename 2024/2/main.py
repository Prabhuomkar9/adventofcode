if __name__ == "__main__":
    # Driver Code
    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()

    ans1, ans2 = 0, 0

    for report in (list(map(int, line.split(" "))) for line in lines):
        diff = [report[i] - report[i - 1] for i in range(1, len(report))]
        sign = 1 if diff[0] > 0 else -1

        if all(abs(d) <= 3 and sign * d > 0 for d in diff):
            ans1 += 1
            ans2 += 1
        else:
            for i, r in enumerate(report):
                report = report[:i] + report[i + 1 :]

                diff = [report[i] - report[i - 1] for i in range(1, len(report))]
                sign = 1 if diff[0] > 0 else -1

                report = report[:i] + [r] + report[i:]

                if all(abs(d) <= 3 and sign * d > 0 for d in diff):
                    ans2 += 1
                    break

    print(ans1, ans2)
