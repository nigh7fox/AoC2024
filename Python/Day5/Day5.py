def readInput():
    with open('test_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def formatPrintQueue():
    lines = readInput()
    pageOrderingRules = []
    printQueue = []
    for i, line in enumerate(lines):
        if line == "":
            print(f"Seperator at: {i}")
            pageOrderingRules = lines[0:i]
            printQueue = lines[i+1:len(lines)]
    return [pageOrderingRules, printQueue]


def getPageRules(rules, pageNum):
    allCurrentPageRules = []
    for rule in rules:
        splitRules = str(rule).split("|")
        for r in splitRules:
            if int(r) == int(pageNum):
                allCurrentPageRules.append(rule)
    return allCurrentPageRules


def controlPrintQueue():
    formattedQueue = formatPrintQueue()
    rules = formattedQueue[0]
    queue = formattedQueue[1]
    for i, pages in enumerate(queue):
        splitPages = pages.split(",")
        print(f"Update: {i} - Page numbers: {splitPages}")
        for page in pages.split(","):
            print(f"Page: {page} - Rules: {getPageRules(rules, page)}")


def main(part):
    if part == 1:
        return controlPrintQueue()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")