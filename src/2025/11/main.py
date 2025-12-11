from argparse import ArgumentParser

import bisect
import collections
import functools
import heapq
import re
import time
import typing


if __name__ == "__main__":
    # Driver Code
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    with open("./test.txt" if args.test else "./input.txt", "r") as file:
        lines = file.read().strip().splitlines()
    st = time.time()

    # Prepare the data here
    graph = collections.defaultdict(list)
    for line in lines:
        devices = line.split()
        graph[devices[0][:-1]] = devices[1:]

    ans1, ans2 = 0, 0

    # Logic goes here
    @functools.lru_cache(None)
    def dfs(device: str, seenDac: bool, seenFft: bool):
        match device:
            case "out":
                return (1, 1 if seenDac and seenFft else 0)
            case "dac":
                seenDac = True
            case "fft":
                seenFft = True
        return (
            sum([dfs(neighbor, seenDac, seenFft)[0] for neighbor in graph[device]]),
            sum([dfs(neighbor, seenDac, seenFft)[1] for neighbor in graph[device]]),
        )

    ans1 = dfs("you", False, False)[0]
    ans2 = dfs("svr", False, False)[1]

    et = time.time()
    print("-t" if args.test else "-i", "t:", round((et - st), 4), ans1, ans2)
