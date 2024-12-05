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
                allCurrentPageRules.append(splitRules)
    return allCurrentPageRules


def getBeforeRules(allCurrentPageRules, pageNum):
    return [rule[1] for i, rule in enumerate(allCurrentPageRules) if allCurrentPageRules[i][0] == pageNum]


def getAfterRules(allCurrentPageRules, pageNum):
    return [rule[0] for i, rule in enumerate(allCurrentPageRules) if allCurrentPageRules[i][1] == pageNum]


def controlPrintQueue():
    formattedQueue = formatPrintQueue()
    rules = formattedQueue[0]
    queue = formattedQueue[1]
    before = []
    after = []
    for x, pages in enumerate(queue):
        splitPages = pages.split(",")
        print("###################")
        print(f"Update: {x} - Page numbers: {splitPages} - Page Queue Length: {len(splitPages)}")
        for y, page in enumerate(splitPages):
            print(f"Page: {splitPages[y]} - Rules: {getPageRules(rules, page)} - Page Queue Index: {y}")
            for z in range(1, len(splitPages)):
                if y + z <= (len(splitPages) - 1):
                    canBeBefore = getBeforeRules(getPageRules(rules, page), page)
                    shouldBeAfter = getAfterRules(getPageRules(rules, page), page)
                    if splitPages[y + z] in canBeBefore:
                        print(splitPages[y + z])
            print(f"Before: {canBeBefore} After: {shouldBeAfter}")
                    # print(splitPages[y + z])
                    # print(int(pages[y + z]))
            print("----------------")
        print("###################")


def main(part):
    if part == 1:
        return controlPrintQueue()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")