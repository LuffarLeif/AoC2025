def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()
    # Split on new line
    rows = [p for p in line.split("\n") if p]
    return rows

def countAdjacent(row, col, rows):
    count = 0
    rowMax = len(rows)
    colMax = len(rows[0])

    # Loop over the 8 adjacent neighbors
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue  # skip itself
            r = row + dr
            c = col + dc
            if 0 <= r < rowMax and 0 <= c < colMax:
                if rows[r][c] == '@':
                    count += 1
    return count


def part1():
    rows = getInput()
    sum = 0
    for row in range(len(rows)):
        for col in range(len(rows[0])):

            if rows[row][col] == '@': # if it is a roll here
                count = countAdjacent(row, col, rows)
                if count < 4:
                    sum += 1
    print(sum)

def part2():
    rows = getInput()
    sum = 0
    removed = True
    while removed: # for as long as something has been removed, continue
        removed = False
        for row in range(len(rows)):
            for col in range(len(rows[0])):

                if rows[row][col] == '@':  # if it is a roll here
                    count = countAdjacent(row, col, rows)
                    if count < 4:
                        rows[row] = rows[row][:col]+'x'+rows[row][col+1:]
                        removed = True
                        sum += 1
    print(sum)

if __name__ == "__main__":
    part1()
    part2()