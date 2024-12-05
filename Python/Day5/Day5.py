def readInput():
    with open('input.txt') as f:
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
    errorsFound = []
    answer = 0
    for x, pages in enumerate(queue):
        splitPages = pages.split(",")
        # print(f"########## Update {x + 1} ##########")
        # print(f"Page numbers: {splitPages} - Page Queue Length: {len(splitPages)}")
        for y, page in enumerate(splitPages):
            # print(f"Page: {splitPages[y]} - Rules: {getPageRules(rules, page)} - Page Queue Index: {y}")
            stillToGo = []
            for z in range(1, len(splitPages)):
                canBeBefore = getBeforeRules(getPageRules(rules, page), page)
                shouldBeAfter = getAfterRules(getPageRules(rules, page), page)
                if y + z <= (len(splitPages) - 1):
                    # print(f"Check against {splitPages[y + z]}")
                    stillToGo.append(splitPages[y + z])
                    if splitPages[y + z] in shouldBeAfter:
                        # print("Abort.")
                        errorsFound.append(x)
                        break
        if x not in set(errorsFound):
            midInt = int(len(splitPages) / 2)
            answer = answer + int(splitPages[midInt])
        #     print(f"Page {splitPages[y]} => Can be before: {canBeBefore} Should be after: {shouldBeAfter}")
        #     print(f"Still remaning in list: {stillToGo}")
        #     print("----------------")
        # print("########## END ###########")
    return answer

def main(part):
    if part == 1:
        return controlPrintQueue()
    return 1


if __name__ == "__main__":
    print(f"Day 3 exercise 1: {main(1)}")
    # print(f"Day 3 exercise 2: {main(2)}")