import math
import os.path
import re

from common.common import DownloadIfNotExists

DownloadIfNotExists("https://adventofcode.com/2022/day/5/input")


# --- Day 5: Supply Stacks ---

def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    with open(filename) as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

        i = 0
        while i < len(lines) and lines[i] != "":
            i += 1

        middle = i

        stacks = []
        input_pattern = re.compile(r"(\d+)")
        m = input_pattern.findall(lines[middle-1])

        for index in [int(ii) for ii in m]:
            stack = []
            h_pos = 1 + ((index-1) * 4)
            for j in range(middle - 2, -1, -1):
                if len(lines[j]) < h_pos or lines[j][h_pos] == "" or lines[j][h_pos].isspace():
                    break
                stack.append(lines[j][h_pos])

            stacks.append(stack)

        #print(stacks)

        input_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
        for move in range(middle + 1, len(lines)):
            m = input_pattern.match(lines[move])

            count = int(m.group(1))
            source = int(m.group(2))
            dest = int(m.group(3))

            if part == 1:
                for i in range(count):
                    stacks[dest-1].append(stacks[source-1].pop())
            else:
                tempStack = []
                for i in range(count):
                    tempStack.append(stacks[source-1].pop())
                for i in range(count):
                    stacks[dest-1].append(tempStack.pop())


        final = "".join([s.pop() for s in stacks])

        print(stacks)

        return final






if __name__ == '__main__':
    process(1, "sample.txt")
