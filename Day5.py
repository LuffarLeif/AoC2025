def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()
    # Split on new line
    arr = [p for p in line.split("\n\n") if p]
    ranges = [p for p in arr[0].split("\n") if p]
    ids = [p for p in arr[1].split("\n") if p]
    return (ranges, ids)

def checkInRange(lower, upper, id):
    if id >= lower and id <= upper:
        return True
    return False

def checkRangeOverlap(range1, range2):
    arr1 = range1.split("-")
    arr2 = range2.split("-")
    if(checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[0])) and not checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[1]))):
        arr1[0] = int(arr2[1])+1
        return str(arr1[0]) + "-" + str(arr1[1])

    elif(not checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[0])) and checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[1]))):
        arr1[1] = int(arr2[0]) - 1
        return str(arr1[0]) + "-" + str(arr1[1])

    elif(checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[0])) and checkInRange(int(arr2[0]), int(arr2[1]), int(arr1[1]))): # completly within, then remove
        return ""

    return range1


def part1():
    sum = 0
    (ranges, ids) = getInput()

    for id in ids:
        for range in ranges:
            arr = range.split("-")
            if checkInRange(int(arr[0]), int(arr[1]), int(id)):
                sum += 1
                break
    print(sum)

def part2():
    (ranges, ids) = getInput() # dont need ids, but reuse getInput() to get ranges
    change = True

    while(change):
        newRanges = [ranges[0]]
        change = False

        for newRange in ranges:
            for range in ranges:

                fixedRange = checkRangeOverlap(newRange, range)

                if fixedRange == "" and newRange != range:
                    ranges.remove(newRange)
                    break

                elif fixedRange != "":
                    if(fixedRange != newRange):
                        newRanges.append(fixedRange)
                        ranges.remove(newRange)
                        ranges.append(fixedRange)
                        change = True
                        break

    ranges = list(set(ranges)) # remove duplicates

    sum = 0
    for range in ranges:
        arr = range.split("-")
        sum = sum + (int(arr[1]) - int(arr[0])+1)

    print(sum)


if __name__ == "__main__":
    part1()
    part2()