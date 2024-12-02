def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def findSmallestAndAdd(nums):
    leftHalf = []
    rightHalf = []
    answer = 0
    for i, num in enumerate(nums):
        splitArr = num.split()
        leftHalf.append(int(splitArr[0]))
        rightHalf.append(int(splitArr[1]))

    while len(leftHalf) >= 2:
        answer = answer + abs((min(rightHalf) - min(leftHalf)))
        # Logs test
        # print(f"Size lists left: {len(leftHalf)} right: {len(rightHalf)}")
        # print(f"Popping left index: {leftHalf.index(min(leftHalf))} right index: {rightHalf.index(min(rightHalf))}")
        # print(f"Add to answer = {min(rightHalf)} - {min(leftHalf)}")
        # print(f"Right: {rightHalf} Left: {leftHalf}")
        if (len(leftHalf) == 2):
            answer = answer + abs((max(rightHalf) - max(leftHalf)))
        leftHalf.pop(leftHalf.index(min(leftHalf)))
        rightHalf.pop(rightHalf.index(min(rightHalf)))
    return answer


def findSmallestAndAddV2(nums):
    leftHalf = []
    rightHalf = []
    answer = 0
    for i, num in enumerate(nums):
        splitArr = num.split()
        leftHalf.append(int(splitArr[0]))
        rightHalf.append(int(splitArr[1]))

    while len(leftHalf) >= 2:
        answer = answer + abs((min(rightHalf) - min(leftHalf)))
        # Logs test
        # print(f"Size lists left: {len(leftHalf)} right: {len(rightHalf)}")
        # print(f"Popping left index: {leftHalf.index(min(leftHalf))} right index: {rightHalf.index(min(rightHalf))}")
        # print(f"Add to answer = {min(rightHalf)} - {min(leftHalf)}")
        # print(f"Right: {rightHalf} Left: {leftHalf}")
        if (len(leftHalf) == 2):
            answer = answer + abs((max(rightHalf) - max(leftHalf)))
        leftHalf.pop(leftHalf.index(min(leftHalf)))
        rightHalf.pop(rightHalf.index(min(rightHalf)))
    return answer


def main(part):
    if part == 1:
        return findSmallestAndAdd(readInput())
    return findSmallestAndAddV2(readInput())


if __name__ == "__main__":
    print(f"Day 1 exercise 1: {main(1)}")
    # print(f"Day 1 exercise 2: {main(2)}")