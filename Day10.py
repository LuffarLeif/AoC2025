from itertools import product
from z3 import Int, Optimize, sat

def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    matrix = []
    rows = [p for p in line.split("\n") if p]
    for row in rows:
        cols = [c for c in row.split(" ") if c]
        matrix.append(cols)

    return matrix


def FindFewestButtons(buttons, b):
    n = len(buttons)
    x = [i for i in product(range(2), repeat=n)]
    fewest = -1

    lamps = [0] * len(b)

    for c in x:
        for j in range(len(c)):
            if c[j] == 1:
                for idx in buttons[j]:
                    lamps[idx] = 1 - lamps[idx] 

        # check success
        success = True
        for i in range(len(lamps)):
            if lamps[i] != b[i]:
                success = False
                break

        if success:
            presses = 0
            for val in c:
                presses += val
            if fewest == -1 or presses < fewest:
                fewest = presses

        # reset lamps
        for i in range(len(lamps)):
            lamps[i] = 0

    return fewest


def part1():
    matrix = getInput()
    sum = 0

    for row in matrix:
        # target lamp pattern b
        b = []
        lamps = row[0] 
        for ch in lamps:
            if ch == '.':
                b.append(0)
            elif ch == '#':
                b.append(1)

        buttons = []
        for i in range(len(row)):
            if i != 0 and i != len(row) - 1:  
                arr = []
                num = ""
                for ch in row[i]:
                    if ch.isdigit():
                        num += ch
                    else:
                        if num != "":
                            arr.append(int(num))
                            num = ""
                if num != "":
                    arr.append(int(num))
                buttons.append(arr)

        val = FindFewestButtons(buttons, b)
        sum += val

    print(sum)


def fewest_presses(buttons, targets):
    n = len(buttons)
    m = len(targets)

    opt = Optimize()
    x = [Int(f"x{i}") for i in range(n)]

    for xi in x:
        opt.add(xi >= 0)

    for k in range(m):
        expr = 0
        for i in range(n):
            if k in buttons[i]:
                expr += x[i]
        opt.add(expr == targets[k])

    opt.minimize(sum(x))

    if opt.check() != sat:
        return -1

    model = opt.model()
    total = 0
    for xi in x:
        total += model[xi].as_long()
    return total


def part2():
    matrix = getInput()
    total = 0

    for row in matrix:
        targets_str = row[-1]
        targets = [int(t) for t in targets_str[1:-1].split(',')]

        buttons = []
        for button in row[1:-1]:
            xs = button[1:-1].split(',')
            buttons.append([int(v) for v in xs if v])

        cost = fewest_presses(buttons, targets)
        total += cost

    print(total)



if __name__ == "__main__":
    part1()
    part2()
