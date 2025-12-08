def getInput():
    points = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str, z_str = line.split(",")
            points.append((int(x_str), int(y_str), int(z_str)))
    return points


def part1():
    points = getInput()
    n = len(points)

    # Build all pairs with squared distances
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            edges.append((dist2, i, j))

    # Sort by distance
    edges.sort(key=lambda e: e[0])

    # Disjoint set / union-find
    parent = [i for i in range(n)]
    size = [1] * n

    def find(x):
        # Path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # Union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Process the 1000 closest pairs (or fewer if not enough)
    num_pairs = min(1000, len(edges))
    for k in range(num_pairs):
        _, i, j = edges[k]
        union(i, j)

    # Collect sizes of all circuits (unique roots)
    seen = set()
    circuit_sizes = []
    for i in range(n):
        r = find(i)
        if r not in seen:
            seen.add(r)
            circuit_sizes.append(size[r])

    circuit_sizes.sort(reverse=True)
    a = circuit_sizes[0]
    b = circuit_sizes[1]
    c = circuit_sizes[2]
    answer = a * b * c

    print(answer)

def part2():
    points = getInput()
    n = len(points)

    # Build all pairs with squared distances
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            edges.append((dist2, i, j))

    # Sort by distance (closest first)
    edges.sort(key=lambda e: e[0])

    # Disjoint set / union-find
    parent = [i for i in range(n)]
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False  # no merge
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True  # merged

    components = n
    last_i = -1
    last_j = -1

    # Process edges until everything is in one circuit
    for dist2, i, j in edges:
        if union(i, j):
            components -= 1
            last_i = i
            last_j = j
            if components == 1:
                break

    # last_i, last_j are the last pair that merged everything
    x1 = points[last_i][0]
    x2 = points[last_j][0]
    answer = x1 * x2
    print(answer)

if __name__ == "__main__":
    part1()
    part2()
