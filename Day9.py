def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()
    # Split on new line
    list = [[int(val) for val in p.split(',') if val] for p in line.split("\n") if p]

    return list

def part1():
    coords = getInput()
    max_area = 0

    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i + 1, len(coords)):
            x2, y2 = coords[j]
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area

    print(max_area)

def buildInsideRanges(coords):
    inside = {}

    n = len(coords)
    edges = []
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+1) % n]
        edges.append((x1, y1, x2, y2))

    minY = min(y for x, y in coords)
    maxY = max(y for x, y in coords)

    for y in range(minY, maxY + 1):
        xs = []

        for (x1, y1, x2, y2) in edges:
            if x1 == x2:
                lo = min(y1, y2)
                hi = max(y1, y2)

                if lo <= y < hi:
                    xs.append(x1)

        xs.sort()

        if len(xs) >= 2:
            row_ranges = []
            for i in range(0, len(xs) - 1, 2):
                xlo = xs[i]
                xhi = xs[i+1]
                if xlo > xhi:
                    xlo, xhi = xhi, xlo
                row_ranges.append((xlo, xhi))
            inside[y] = row_ranges

    return inside

def rowCovers(inside, y, x1, x2):
    if y not in inside:
        return False
    for (a, b) in inside[y]:
        if a <= x1 and x2 <= b:
            return True
    return False


def rectInside(inside, x1, y1, x2, y2):
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)

    for y in range(ymin, ymax + 1):
        if not rowCovers(inside, y, xmin, xmax):
            return False
    return True

def part2():
    coords = getInput()
    inside = buildInsideRanges(coords)

    max_area = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i + 1, len(coords)):
            x2, y2 = coords[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area <= max_area:
                continue

            if rectInside(inside, x1, y1, x2, y2):
                max_area = area

    print(max_area)



if __name__ == "__main__":
    part1()
    part2() # part two solution is naive and slow but should finish within 1-2 min, I dont have time to improve its time complexity atm