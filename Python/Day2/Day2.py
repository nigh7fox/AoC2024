def readInput():
    with open('test_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def evalReports(reports):
    levels = [report.split(" ") for report in reports]
    intLevels = [list(map(int, lvl)) for lvl in levels]
    levelsDiff = getLevelDiff(intLevels)
    return getMinMaxDiff(levelsDiff, True)


def evalReportsV2(reports):
    levels = [report.split(" ") for report in reports]
    intLevels = [list(map(int, lvl)) for lvl in levels]
    badLevels = []
    levelsDiff = getLevelDiff(intLevels)
    levelsMinMaxDiff = getMinMaxDiff(levelsDiff, False, [])
    for x in intLevels:
        if type(levelsMinMaxDiff) is list:
            if (levelsMinMaxDiff[0] in badLevels):
                print(f"Second run for level {levelsMinMaxDiff[0]}, if error is found record as level as unsafe")
                levelsDiff = getLevelDiff(intLevels)
                levelsMinMaxDiff = getMinMaxDiff(levelsDiff, True, badLevels)
            else:
                print(f"Error found! Trying to rerun Level {levelsMinMaxDiff[0]} by removing {levelsMinMaxDiff[1]}")
                print(f"Rerunning get min max")
                badLevels.append(levelsMinMaxDiff[0])
                intLevels[levelsMinMaxDiff[0]].pop(levelsMinMaxDiff[1])
                levelsDiff = getLevelDiff(intLevels)
                levelsMinMaxDiff = getMinMaxDiff(levelsDiff, False, badLevels)
    return levelsMinMaxDiff


# Get level differences
def getLevelDiff(intLevels):
    levelsDiff = []
    for _, levels in enumerate(intLevels):
        levelDiff = []
        for x, _ in enumerate(levels):
            if (x != len(levels) - 1):
                levelDiff.append((levels[x] - levels[x + 1]))
        levelsDiff.append(levelDiff)
    return levelsDiff


# Get max min differences in order to determine if allowed
def getMinMaxDiff(levelsDiff, rerun=False, badLevels=None):
    levelsAreSafe = []
    error = []
    for x, diff in enumerate(levelsDiff):
        print(f"Level {x} diffs: {levelsDiff[x]}")
        # init level is safe
        levelIsSafe = 1
        checkIncrDecr = checkIncreasingDecreasing(x, diff)
        if type(checkIncrDecr) is list:
            levelIsSafe = 0
            error.append(checkIncrDecr)
        if(min(diff) == 0 and x not in badLevels):
            # return error with level and index to pop
            levelIsSafe = 0
            error.append([x, list(diff).index(min(diff))])
            print(f"Error => zero diff: {list(diff).index(min(diff))}")
        if (abs(max(diff)) >= 1 and abs(max(diff) <= 3) and abs(min(diff)) <= 3):
            levelIsSafe = 1     
        else:
            levelIsSafe = 0
            
        levelsAreSafe.append(levelIsSafe)
        # levelsIsSafe = checkIncreasingDecreasing(diff)
    if rerun is True:
        error = []
    if len(error) != 0:
        return error[0]
    return sum(levelsAreSafe)


def checkIncreasingDecreasing(x, diff):
    # for each number check if it's positive or negative
    # the amount of count should be equal to len of diff array
    # this means all numbers are either all positive or all negative
    intCount = 0
    intCountArr = []
    for num in diff:
        if num < 0:
            intCountArr.append(1)
            intCount = intCount + 1
        else:
            intCountArr.append(0)
    if intCount != len(diff) and intCount != 0:
        print(f"Error => increase/decrease at Level {x} index {intCountArr.index(0)}")
        return [x, intCountArr.index(0)]
    return False


def main(part):
    if part == 1:
        return evalReports(readInput())
    return evalReportsV2(readInput())


if __name__ == "__main__":
    # print(f"Day 2 exercise 1: {main(1)}")
    print(f"Day 2 exercise 2: {main(2)}")