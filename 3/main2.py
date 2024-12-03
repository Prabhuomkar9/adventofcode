if __name__ == "__main__":
    # Driver Code
    content = ""

    with open("./input.txt", "r") as file:
        content = file.read()

    def initIdentifiers():
        return {
            "d": False,
            "o": False,
            "n": False,
            "'": False,
            "t": False,
            "m": False,
            "u": False,
            "l": False,
            "(": False,
            "n1": (False, 0),
            ",": False,
            "n2": (False, 0),
        }

    identifiers = initIdentifiers()

    allowed, ans = True, 0

    for c in content:
        match c:
            case "d":
                identifiers = initIdentifiers()
                identifiers["d"] = True
            case "o":
                if identifiers["d"]:
                    identifiers["o"] = True
                else:
                    identifiers = initIdentifiers()
            case "n":
                if identifiers["o"]:
                    identifiers["n"] = True
                else:
                    identifiers = initIdentifiers()
            case "'":
                if identifiers["n"]:
                    identifiers["'"] = True
                else:
                    identifiers = initIdentifiers()
            case "t":
                if identifiers["'"]:
                    identifiers["t"] = True
                else:
                    identifiers = initIdentifiers()
            case "m":
                identifiers = initIdentifiers()
                identifiers["m"] = True
            case "u":
                if identifiers["m"]:
                    identifiers["u"] = True
                else:
                    identifiers = initIdentifiers()
            case "l":
                if identifiers["u"]:
                    identifiers["l"] = True
                else:
                    identifiers = initIdentifiers()
            case "(":
                if identifiers["l"] or identifiers["o"] or identifiers["t"]:
                    identifiers["("] = True
                else:
                    identifiers = initIdentifiers()
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                if identifiers["m"] and identifiers["("]:
                    if not identifiers[","]:
                        num = identifiers["n1"][1] * 10 + int(c)
                        if num < 1000:
                            identifiers["n1"] = (True, num)
                        else:
                            identifiers = initIdentifiers()
                    else:
                        num = identifiers["n2"][1] * 10 + int(c)
                        if num < 1000:
                            identifiers["n2"] = (True, num)
                        else:
                            identifiers = initIdentifiers()
                else:
                    identifiers = initIdentifiers()
            case ",":
                if identifiers["n1"][0]:
                    identifiers[","] = True
                else:
                    identifiers = initIdentifiers()
            case ")":
                if identifiers["n2"][0]:
                    if allowed:
                        ans += identifiers["n1"][1] * identifiers["n2"][1]
                elif identifiers["d"] and identifiers["("]:
                    allowed = not identifiers["n"]
                identifiers = initIdentifiers()
            case _:
                identifiers = initIdentifiers()
                identifiers = initIdentifiers()

    print(ans)
