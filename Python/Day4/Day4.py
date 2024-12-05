import re


def readInput():
    with open('test_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def findXmas():
    # horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    xCount = 0
    mCount = 0
    aCount = 0
    sCount = 0
    for line in readInput():
        print(line)
        xCount = xCount + line.count("X")
        mCount = mCount + line.count("M")
        aCount = aCount + line.count("A")
        sCount = sCount + line.count("S")
    print(f"Letters count X: {xCount} M: {mCount} A: {aCount} S: {sCount}")
    return 0


def main(part):
    if part == 1:
        return findXmas()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")