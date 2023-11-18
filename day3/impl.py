import math
import os.path

from common.common import DownloadIfNotExists

DownloadIfNotExists("https://adventofcode.com/2022/day/3/input")

# --- Day 3: Rucksack Reorganization ---

def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    with open(filename) as f:
        lines = f.readlines()

        finalScore_part1 = 0
        finalScore_part2 = 0
        for i, line in enumerate(lines):
            line = line.replace("\n", "")

            if part == 1:
                part1 = line[0:math.ceil(len(line)/2)]
                part2 = line[math.ceil(len(line)/2):]

                finalScore_part1 += score(findCommonLetters(part1, part2))
            elif (i+1) % 3 == 0:
                part1 = lines[i-2].replace("\n", "")
                part2 = lines[i-1].replace("\n", "")
                part3 = lines[i].replace("\n", "")

                finalScore_part2 += score(findCommonLetters2(part1, part2, part3))

        if part == 1:
            return finalScore_part1
        return finalScore_part2

def findCommonLetters(part1, part2):
    for c in part1:
        for c2 in part2:
            if c == c2:
                print(f"Found {c} in both parts ! Adding {score(c)} to final score...")
                return c

def findCommonLetters2(part1, part2, part3):

    for c in part1:
        currentCommon = ""
        for c2 in part2:
            if c == c2:
                currentCommon = c
        for c3 in part3:
            if c == c3 and c == currentCommon:
                print(f"Found {c} in three parts ! Adding {score(c3)} to final score...")
                return c3

def score(letter):
    code = ord(letter)
    if 97 <= code <= 122:
        return code - 96
    elif 65 <= code <= 90:
        return code - 38
    return 0

if __name__ == '__main__':
    process(1, "sample.txt")