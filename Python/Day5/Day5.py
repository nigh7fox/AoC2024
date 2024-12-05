def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def printQueue():
    return 0


def main(part):
    if part == 1:
        return printQueue()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")