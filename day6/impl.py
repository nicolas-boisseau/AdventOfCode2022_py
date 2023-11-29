import itertools
import os.path
from py_linq import Enumerable

from common.common import DownloadIfNotExists, DetectCurrentDay

try:
    day = DetectCurrentDay()
    if day != 0:
        DownloadIfNotExists(f"https://adventofcode.com/2022/day/{day}/input")
except:
    pass

def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    with open(filename) as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

        input = lines[0]

        if part == 1:
            return DetectPacket(input, 4)
        else:
            return DetectPacket(input, 14)

def DetectPacket(input, packetSize):
    four_letter_window = input[0:packetSize]
    i = 0
    while (i + packetSize) < len(input) and not IsMarker(four_letter_window, packetSize):
        i += 1
        four_letter_window = input[i:i + packetSize]

    return i + packetSize

def IsMarker(str, packetSize):
    # array = sorted([letter for letter in str])
    # return packetSize == len([k for k, v in itertools.groupby(array)])
    return Enumerable(str).distinct().count() == packetSize

if __name__ == '__main__':
    process(1, "sample.txt")
