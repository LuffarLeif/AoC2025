def getInput():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    # keep all spaces, just strip trailing newlines
    return lines


def part1():
    rows = getInput()
    if not rows:
        print(0)
        return

    height = len(rows)
    width = len(rows[0])

    problem_ranges = []
    in_block = False
    start = 0

    for col in range(width):
        blank = True
        for row in range(height):
            if rows[row][col] != ' ':
                blank = False
                break

        if not blank and not in_block:
            in_block = True
            start = col
        elif blank and in_block:
            # ending a problem block before this column
            in_block = False
            problem_ranges.append((start, col))

    # If the last block goes to the end
    if in_block:
        problem_ranges.append((start, width))

    grand_total = 0

    # Process each problem block
    for (c_start, c_end) in problem_ranges:
        # Find operator in bottom row (last row)
        op_row = height - 1
        op = None
        for col in range(c_start, c_end):
            ch = rows[op_row][col]
            if ch == '+' or ch == '*':
                op = ch
                break

        if op is None:
            # No operator found in this block; skip (or raise error)
            continue

        # Collect numbers from rows above the operator row
        nums = []
        for row in range(0, op_row):
            segment = rows[row][c_start:c_end]
            digits = ""
            for ch in segment:
                if ch.isdigit():
                    digits += ch
            if digits != "":
                nums.append(int(digits))

        if not nums:
            continue

        # Compute value of this problem
        if op == '+':
            value = 0
            for n in nums:
                value += n
        else:  # op == '*'
            value = 1
            for n in nums:
                value *= n

        grand_total += value

    print(grand_total)

def part2():
    rows = getInput()
    if not rows:

        print(0)
        return

    height = len(rows)
    width = len(rows[0])

    problem_ranges = []
    in_block = False
    start = 0

    for col in range(width):
        blank = True
        for row in range(height):
            if rows[row][col] != ' ':
                blank = False
                break

        if not blank and not in_block:
            in_block = True
            start = col
        elif blank and in_block:
            in_block = False
            problem_ranges.append((start, col))

    if in_block:
        problem_ranges.append((start, width))

    grand_total = 0

    for (c_start, c_end) in problem_ranges:
            # Find operator in bottom row (last row)
        op_row = height - 1
        op = None
        for col in range(c_start, c_end):
            ch = rows[op_row][col]
            if ch == '+' or ch == '*':
                op = ch
                break

        if op is None:
            continue

        # Collect numbers by columns, RIGHT to LEFT
        nums = []
        for col in range(c_end - 1, c_start - 1, -1):
            digits = ""
            for row in range(0, op_row):
                ch = rows[row][col]
                if ch.isdigit():
                    digits += ch
            if digits != "":
                nums.append(int(digits))

        if not nums:
            continue

         # Compute this problem's value
        if op == '+':
            value = 0
            for n in nums:
                value += n
        else:  # op == '*'
            value = 1
            for n in nums:
                value *= n

        grand_total += value

    print(grand_total)


if __name__ == "__main__":
    part1()
    part2()