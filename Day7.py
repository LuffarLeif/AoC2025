def getInput():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    return lines


def part1():
    rows = getInput()
    R = len(rows)
    C = len(rows[0])

    # Find S
    start_row = start_col = None
    for r in range(R):
        c = rows[r].find('S')
        if c != -1:
            start_row, start_col = r, c
            break

    if start_row is None:
        print("No S found")
        return

    stack = []
    if start_row + 1 < R:
        stack.append((start_row + 1, start_col))

    visited = set()
    splits = 0

    while stack:
        r, c = stack.pop()

        if r < 0 or r >= R or c < 0 or c >= C:
            continue

        if (r, c) in visited:
            continue
        visited.add((r, c))

        cell = rows[r][c]

        if cell == '.':
            # Continue straight down
            stack.append((r + 1, c))

        elif cell == '^':
            # Split here
            splits += 1
            if c - 1 >= 0:
                stack.append((r, c - 1))
            if c + 1 < C:
                stack.append((r, c + 1))

        elif cell == 'S':
            # Just in case, treat S like empty below
            stack.append((r + 1, c))


    print(splits)


def part2():
    rows = getInput()
    R = len(rows)
    C = len(rows[0])

    # Find S
    start_row = start_col = None
    for r in range(R):
        c = rows[r].find('S')
        if c != -1:
            start_row, start_col = r, c
            break

    if start_row is None:
        print("No S found")
        return

    if start_row == R - 1:
        print(1)
        return

    cache = {}

    def ways(r, c):
        key = (r, c)
        if key in cache:
            return cache[key]

        ch = rows[r][c]

        if ch == '.' or ch == 'S':
            if r == R - 1:
                # Leaving the bottom: one completed timeline
                result = 1
            else:
                result = ways(r + 1, c)

        elif ch == '^':
            total = 0
            # Left branch
            if c - 1 < 0:
                total += 1
            else:
                total += ways(r, c - 1)

            # Right branch
            if c + 1 >= C:
                total += 1
            else:
                total += ways(r, c + 1)

            result = total

        else:
            if r == R - 1:
                result = 1
            else:
                result = ways(r + 1, c)

        cache[key] = result
        return result

    # Start just below S, moving downwards
    answer = ways(start_row + 1, start_col)
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
