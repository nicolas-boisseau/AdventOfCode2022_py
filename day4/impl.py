import math
import os.path
import re

from common.common import DownloadIfNotExists

DownloadIfNotExists("https://adventofcode.com/2022/day/4/input")

# --- Day 4: Camp Cleanup ---

def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    with open(filename) as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

        nb_pair = 0
        input_pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
        for line in lines:
            m = input_pattern.match(line)

            a1 = int(m.group(1))
            b1 = int(m.group(2))
            a2 = int(m.group(3))
            b2 = int(m.group(4))

            if part == 1:
                if a2 <= a1 <= b2 and a2 <= b1 <= b2:
                    nb_pair += 1
                elif a1 <= a2 <= b1 and a1 <= b2 <= b1:
                    nb_pair += 1
            else:
                if a2 <= a1 <= b2 or a2 <= b1 <= b2:
                    nb_pair += 1
                elif a1 <= a2 <= b1 or a1 <= b2 <= b1:
                    nb_pair += 1

        return nb_pair


if __name__ == '__main__':
    process(1, "sample.txt")
