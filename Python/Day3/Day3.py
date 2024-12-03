import re


def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def mulAoc(numArr):
    return (int(numArr[0])*int(numArr[1]))


def parseInput():
    answer = 0
    cmdsArr = []
    # print(len(cmd))
    for commands in readInput():
        cmds = re.findall(r"mul\(\d+,\d+\)", commands)
        for cmd in cmds:
            regInt = re.sub(r"[^0-9]", " ", cmd)[4:].split(" ")[0:2]
            answer = answer + mulAoc(regInt)
    return answer


def main(part):
    if part == 1:
        return parseInput()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")