def readInput():
    with open('test_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def formGridFromInput(lines):
    grid = []
    for x, line in enumerate(lines):
        currRowList = list(lines[x])
        grid.append(currRowList) 
    return grid


def gridToLine(grid):
    lines = []
    for y in grid:
        line = ''.join(y)
        lines.append(line)
    return lines

def displayGrid(grid):
    for i, x in enumerate(grid):
        print(f"{i}: {x}")


def guardGallivant(lines):
    answer = 0
    currentPosition = []
    grid = formGridFromInput(lines)
    reachedTheEnd = False
    while reachedTheEnd is False:
    # for x in range(5): # RUN INDIVIDUAL TEST
        # print(f"Grid before:")
        # displayGrid(grid)
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                for i in range(len(row)):
                    match lines[x][y]:
                        case "^":
                            currentPosition = [x, y]
                            if (x - i) < 0:
                                reachedTheEnd = True
                            if (x - i) >= 0:
                                # print(f"Current position {currentPosition} pointing upwards")
                                nextLetterVerticalUp = lines[x - i][y]
                                if nextLetterVerticalUp != "#":
                                    # print(f"Can move to {nextLetterVerticalUp} coordinates [{x - i}, {y}]")
                                    # print(f"Moving up 1 step")
                                    grid[x - i][y] = "X"
                                else:
                                    # print(f"Found an obstacle at coordinates [{x - i}, {y}] turning 90 degrees")
                                    # print(f"Now pointing to the right")
                                    grid[x - (i - 1)][y] = ">"
                                    break
                        case ">":
                            # Check if add the end of grid
                            if (y + i) > len(row):
                                reachedTheEnd = True
                            currentPosition = [x, y]
                            # print(f"Current position {currentPosition} pointing to the right")
                            if (y + i) <= len(row) - 1:
                                nextLetterHorizontal = lines[x][y + i]
                                if nextLetterHorizontal != "#":
                                    # print(f"Can move to {nextLetterHorizontal} coordinates [{x}, {y + i}]")
                                    # print(f"Moving up 1 step")
                                    grid[x][y + i] = "X"
                                else:
                                    # print(f"Found an obstacle at coordinates [{x - i}, {y}] turning 90 degrees")
                                    # print(f"Now pointing down")
                                    grid[x][y + (i - 1)] = "v"
                                    break
                        case "<":
                            # Check if add the end of grid
                            if (y - i) < 0:
                                reachedTheEnd = True
                            currentPosition = [x, y]
                            # print(f"Current position {currentPosition} pointing to the left")
                            if (y - i) >= 0:
                                nextLetterBackwards = lines[x][y - i]
                                if nextLetterBackwards != "#":
                                    # print(f"Can move to {nextLetterBackwards} coordinates [{x}, {y - i}]")
                                    # print(f"Moving up 1 step")
                                    grid[x][y - i] = "X"
                                else:
                                    # print(f"Found an obstacle at coordinates [{x}, {y - i}] turning 90 degrees")
                                    # print(f"Now pointing up")
                                    grid[x][y - (i - 1)] = "^"
                                    break
                        case "v":
                            # Check if add the end of grid
                            if (x + i) > len(lines):
                                reachedTheEnd = True
                            currentPosition = [x, y]
                            # print(f"Current position {currentPosition} pointing downwards")
                            if (x + i) <= len(lines) - 1:
                                nextLetterVerticalDown = lines[x + i][y]
                                if nextLetterVerticalDown != "#":
                                    # print(f"Can move to {nextLetterVerticalDown} coordinates [{x + i}, {y}]")
                                    # print(f"Moving up 1 step")
                                    grid[x + i][y] = "X"
                                else:
                                    # print(f"Found an obstacle at coordinates [{x + i}, {y - i}] turning 90 degrees")
                                    # print(f"Now pointing to the left")
                                    grid[x + (i - 1)][y] = "<"
                                    break
        # print(f"Grid after:")
        # displayGrid(grid)
        lines = gridToLine(grid)
    
    for line in lines:
        answer = answer + str(line).count("X")

    return answer

def main(part):
    lines = readInput()
    if part == 1:
        return guardGallivant(lines)
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")