if __name__ == "__main__":
    # Driver Code
    equation = []

    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()
        equation = list(map(lambda l: l.split(), lines))

    ans = 0

    for res, *a in equation:
        res = int(res[:-1])
        a = list(map(int, a))

        def dfs(i, cRes, op):
            if cRes > res:
                return 0

            if i == len(a):
                return res if cRes == res else 0

            nRes = (
                cRes + a[i]
                if op == "+"
                else cRes * a[i] if op == "*" else int(f"{cRes}{a[i]}")
            )

            l = dfs(i + 1, nRes, "+")
            if l > 0:
                return l
            else:
                r = dfs(i + 1, nRes, "*")
                if r > 0:
                    return r
                else:
                    return dfs(i + 1, nRes, "|")

        l = dfs(1, a[0], "+")
        if l > 0:
            ans += l
        else:
            r = dfs(1, a[0], "*")
            if r > 0:
                ans += r
            else:
                ans += dfs(1, a[0], "|")

    print(ans)
