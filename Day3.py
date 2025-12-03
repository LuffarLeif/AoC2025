
def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()
    # Split on new line
    banks = [p for p in line.split("\n") if p]
    return banks

def part1():
    sum = 0
    banks = getInput()
    for bank in banks:
        mostSignificant = 0
        mostSignificantIndex = 0
        for i in range(len(bank)-1): # -1 because it cannot be the last battery in bank
            value = int(bank[i])
            if value > mostSignificant:
                mostSignificant = value
                mostSignificantIndex = i

        leastSignificant = 0
        for i in range (mostSignificantIndex+1, len(bank)):
            value = int(bank[i])
            if value > leastSignificant:
                leastSignificant = value

        sum = sum + 10*mostSignificant + leastSignificant

    print(sum)

def part2():
    sum = 0
    banks = getInput()

    for bank in banks:
        to_remove = len(bank) - 12 # should be 100-12 = 88
        stack = ""

        for ch in bank:

            while to_remove > 0 and len(stack) > 0 and stack[-1] < ch:
                stack = stack[:-1]    # pop last char
                to_remove -= 1

            stack = stack + ch

        # If we still have to remove digits, remove them from the end
        if to_remove > 0:
            stack = stack[:-to_remove]

        sum = sum + int(stack)

    print(sum)

if __name__ == "__main__":
    part1()
    part2()