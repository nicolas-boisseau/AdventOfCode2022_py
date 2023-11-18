import os.path

from common.common import DownloadIfNotExists

DownloadIfNotExists("https://adventofcode.com/2022/day/2/input")

# --- Day 2: Rock Paper Scissors ---

them_Set = {
    'A': "Rock",  # Rock
    'B': "Paper",  # Paper
    'C': "Scissors"  # Scissors
}
toWin = {
    "Rock": "Paper",  # Rock
    "Paper": "Scissors",  # Paper
    "Scissors": "Rock"  # Scissors
}
toLose = {
    "Rock": "Scissors",  # Rock
    "Paper": "Rock",  # Paper
    "Scissors": "Paper"  # Scissors
}
us_Set = {
    'X': "Rock",  # Rock
    'Y': "Paper",  # Paper
    'Z': "Scissors"  # Scissors
}
points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}


def process(part, filename):
    if not (os.path.exists(filename)):
        print("Input file not found !")

    print("Input file OK ! Starting processing...")
    part1 = part2 = 0
    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            #split = line.replace("\n", "").split(" ")
            #print(split)
            them_raw = line[0]
            us_raw = line[2]
            them = them_Set[them_raw]
            us = us_Set[us_raw]

            #print(f"J1: {us} - J2: {them}")

            part1 += points[us]
            if us == them:  # Draw
                part1 += 3
            else:
                game = us + "-" + them
                if game == "Rock-Scissors" or game == "Paper-Rock" or game == "Scissors-Paper":  # Win
                    part1 += 6

            if us_raw == 'X':
                play = toLose[them]
                part2 += points[play]
            elif us_raw == 'Z':
                play = toWin[them]
                part2 += points[play] + 6
            else:
                part2 += points[them] + 3

    if part == 1:
        return part1
    else:
        return part2
