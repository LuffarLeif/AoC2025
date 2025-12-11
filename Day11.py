from functools import lru_cache

graph = {}

def getInput():
    global graph
    graph = {}
    with open("input.txt", "r") as f:
        line = f.read().strip()
    rows = [p for p in line.split("\n") if p]

    for row in rows:
        entry = row.split(':')
        key = entry[0].strip()
        if len(entry) > 1:
            value = entry[1].split()
        else:
            value = []
        graph[key] = value

def findNext(value):
    if value == "out":
        return 1
    else:
        total = 0
        for next in graph.get(value):
            total += findNext(next)
        return total

@lru_cache(maxsize=None)
def findNextExtened(value, dac, fft):

    if value == "dac":
        dac = True
    if value == "fft":
        fft = True
    if value == "out":
        if(dac and fft):
            return 1
        return 0
    else:
        total = 0
        for next in graph.get(value):
            total += findNextExtened(next, dac, fft)
        return total

def part1():
    global sum

    total = findNext("you")
    
    print(total)

def part2():
    global sum2

    total = findNextExtened("svr", False, False)
    
    print(total)
    
if __name__ == "__main__":
    getInput()

    part1()
    part2()
    