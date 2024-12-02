def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def evalReports(reports):
    levels = [report.split(" ") for report in reports]
    intLevels = [list(map(int, lvl)) for lvl in levels]
    levelsDiff = []
    levelsAreSafe = []
    for i, levels in enumerate(intLevels):
        levelDiff = []
        for x, level in enumerate(levels):
            if (x != len(levels) - 1):
                levelDiff.append((levels[x] - levels[x + 1]))
        levelsDiff.append(levelDiff)
    
    for i, diff in enumerate(levelsDiff):
        levelIsSafe = 1
        if(min(diff) == 0):
            levelIsSafe = 0
        elif (abs(max(diff)) >= 1 and abs(max(diff) <= 3) and abs(min(diff)) <= 3):
            levelIsSafe = 1
        else:
            levelIsSafe = 0

        intCount = 0
        for num in diff:
            if num < 0:
                intCount = intCount + 1
        if intCount != len(diff) and intCount != 0:
            levelIsSafe = 0

        levelsAreSafe.append(levelIsSafe)
    return sum(levelsAreSafe)


def evalReportsV2(reports):
    levels = [report.split(" ") for report in reports]
    intLevels = [list(map(int, lvl)) for lvl in levels]
    levelsDiff = []
    levelsAreSafe = []
    for i, levels in enumerate(intLevels):
        levelDiff = []
        for x, level in enumerate(levels):
            if (x != len(levels) - 1):
                levelDiff.append((levels[x] - levels[x + 1]))
        levelsDiff.append(levelDiff)
    
    for i, diff in enumerate(levelsDiff):
        levelIsSafe = 1
        if(min(diff) == 0):
            levelIsSafe = 0
        elif (abs(max(diff)) >= 1 and abs(max(diff) <= 3) and abs(min(diff)) <= 3):
            levelIsSafe = 1
        else:
            levelIsSafe = 0

        intCount = 0
        for num in diff:
            if num < 0:
                intCount = intCount + 1
        if intCount != len(diff) and intCount != 0:
            levelIsSafe = 0

        levelsAreSafe.append(levelIsSafe)
    return sum(levelsAreSafe)


def main(part):
    if part == 1:
        return evalReports(readInput())
    return evalReportsV2(readInput())


if __name__ == "__main__":
    print(f"Day 2 exercise 1: {main(1)}")
    # print(f"Day 2 exercise 2: {main(2)}")