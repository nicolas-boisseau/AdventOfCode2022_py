import os.path

from common.common import DownloadIfNotExists

DownloadIfNotExists("https://adventofcode.com/2022/day/1/input")


# --- Day 1: Calorie Counting ---

def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    with open(filename) as f:
        lines = f.readlines()

        elves = []
        current = []
        for line in lines:
            if line == "\n":
                elves.append(sum(current))
                current = []
                continue
            current.append(int(line))
        elves.append(sum(current))

        if part == 1:
            return max(elves)
        else:
            elves.sort(reverse=True)
            return elves[0] + elves[1] + elves[2]
