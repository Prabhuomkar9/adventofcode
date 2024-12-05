from collections import defaultdict

if __name__ == "__main__":
    # Driver Code
    rules = defaultdict(set)
    pages = []

    with open("./input.txt", "r") as file:
        content = file.read().splitlines()
        idx = content.index("")
        for i in content[:idx]:
            l, r = i.split("|")
            rules[l].add(r)
        pages = [i.split(",") for i in content[idx + 1 :]]

    def customSort(page: list[str]) -> list[str]:
        for j in range(1, len(page)):
            i = j - 1
            key = page[j]
            while i >= 0 and page[i] not in rules[key]:
                page[i + 1] = page[i]
                i -= 1
            page[i + 1] = key
        print(page)
        return page

    ans = 0

    for page in pages:
        flag = False
        for j in range(1, len(page)):
            i = j - 1
            if page[i] in rules[page[j]]:
                flag = True
                break
        if flag:
            page = customSort(page)
            ans += int(page[len(page) // 2])

    print(ans)
