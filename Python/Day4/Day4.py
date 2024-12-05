import re


def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def findXmas():
    # horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    count = 0
    lines = readInput()
    startingCoords = []
    for x, line in enumerate(lines):
        print(line)
        for y, _ in enumerate(line):
            if lines[x][y] == "X":
                startingCoords.append([x, y])
                print(f"Starting position X: [{x}, {y}]")
                print(f"Starting found count: {count}")
                horizontalWord = ""
                backwardsWord = ""
                verticalWordDown = ""
                verticalWordUp = ""
                diagonalWordLeftUp = ""
                diagonalWordLeftDown = ""
                diagonalWordRightUp = ""
                diagonalWordRightDown = ""
                for i in range(1, 4):
                    # Left to right
                    if (y + i) <= len(lines) - 1:
                        nextLetterHorizontal = lines[x][y + i]
                        horizontalWord += lines[x][y + i]
                        # print(f"Next horizontal letters: {nextLetterHorizontal} coords: [{x}, {y + i}] index: {i}")
                    # Right to left
                    if (x + i) <= len(line) - 1:
                        nextLetterVerticalDown = lines[x + i][y]
                        verticalWordDown += lines[x + i][y]
                        # print(f"Next vertical letters: {nextLetterVertical} coords: [{x + i}, {y}] index: {i}")
                    # Up
                    if (x - i) >= 0:
                        nextLetterVerticalUp = lines[x - i][y]
                        verticalWordUp += lines[x - i][y]
                        # print(f"Next vertical letters: {nextLetterVerticalUp} coords: [{x - i}, {y}] index: {i}")
                    # Down
                    if (y - i) >= 0:
                        nextLetterBackwards = lines[x][y - i]
                        backwardsWord += lines[x][y - i]
                        # print(f"Next backwards letters: {nextLetterBackwards} coords: [{x}, {y - i}] index: {i}")
                    # Diagonal down to the right
                    if (x + i) <= len(line) - 1 and (y + i) <= len(lines) - 1:
                        nextLetterDiagonalDownRight = lines[x + i][y + i]
                        diagonalWordRightDown += lines[x + i][y + i]
                        # print(f"Next diagonal letters: {nextLetterDiagonalDown} coords: [{x + i}, {y + i}] index: {i}")
                    # Diagonal down to the left
                    if (x + i) <= len(line) - 1 and (y - i) >= 0:
                        nextLetterDiagonalDown = lines[x + i][y - i]
                        diagonalWordLeftDown += lines[x + i][y - i]
                        # print(f"Next diagonal letters: {nextLetterDiagonalDown} coords: [{x + i}, {y + i}] index: {i}")
                    # Diagonal up to the left
                    if (x - i) >= 0 and (y - i) >= 0:
                        nextLetterDiagonalLeftUp = lines[x - i][y - i]
                        diagonalWordLeftUp += lines[x - i][y - i]
                        # print(f"Next diagonal letters: {nextLetterDiagonalUp} coords: [{x - i}, {y - i}] index: {i}")
                    # Diagonal up to the right
                    if (x - i) >= 0 and (y + i)  <= len(lines) - 1:
                        nextLetterDiagonalDown = lines[x - i][y + i]
                        diagonalWordRightUp += lines[x - i][y + i]
                        # print(f"Next diagonal letters: {nextLetterDiagonalUp} coords: [{x - i}, {y - i}] index: {i}")
                if (horizontalWord == "MAS"):
                    count = count + 1
                if (verticalWordUp == "MAS"):
                    count = count + 1
                if (verticalWordDown == "MAS"):
                    count = count + 1
                if (diagonalWordLeftDown == "MAS"):
                    count = count + 1
                if (diagonalWordLeftUp == "MAS"):
                    count = count + 1
                if (diagonalWordRightDown == "MAS"):
                    count = count + 1
                if (diagonalWordRightUp == "MAS"):
                    count = count + 1
                if (backwardsWord == "MAS"):
                    count = count + 1
                print(f"Horizontal next 3: {horizontalWord}")
                print(f"Vertical down next 3: {verticalWordDown}")
                print(f"Vertical up next 3: {verticalWordUp}")
                print(f"Diagonal down left next 3: {diagonalWordLeftDown}")
                print(f"Diagonal down right next 3: {diagonalWordRightDown}")
                print(f"Diagonal up left next 3: {diagonalWordLeftUp}")
                print(f"Diagonal up right next 3: {diagonalWordRightUp}")
                print(f"Backwards next 3: {backwardsWord}")
                print(f"Found xmas count: {count}")
                print('--------------')
    print(f"Starting coordinates: {startingCoords}")
    return count


def main(part):
    if part == 1:
        return findXmas()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")