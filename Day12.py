def getInput():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    blocks = [p for p in line.split("\n\n") if p]

    shape_blocks = blocks[:-1]
    shapes = []
    for block in shape_blocks:
        lines = [r for r in block.split("\n") if r]
        grid = lines[1:]          # skip "0:"
        shapes.append(grid)

    regions = [r for r in blocks[-1].split("\n") if r]
    return (shapes, regions)


def parseRegion(line):
    left, right = line.split(":")
    w_str, h_str = left.split("x")
    width = int(w_str)
    height = int(h_str)
    counts = [int(x) for x in right.split()]
    return width, height, counts


def rotate(grid):
    h = len(grid)
    w = len(grid[0])
    out = []
    for c in range(w):
        s = ""
        for r in range(h - 1, -1, -1):
            s += grid[r][c]
        out.append(s)
    return out


def flipH(grid):
    out = []
    for row in grid:
        out.append(row[::-1])
    return out


def normalize_cells(cells):
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    out = []
    for r, c in cells:
        out.append((r - min_r, c - min_c))
    out.sort()
    return tuple(out)


def grid_to_cells(grid):
    cells = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                cells.append((r, c))
    return normalize_cells(cells)


def get_orientations(shape_grid):
    seen = set()
    out = []
    g = shape_grid

    for _ in range(4):
        cells = grid_to_cells(g)
        if cells not in seen:
            seen.add(cells)
            out.append(cells)

        fg = flipH(g)
        cells2 = grid_to_cells(fg)
        if cells2 not in seen:
            seen.add(cells2)
            out.append(cells2)

        g = rotate(g)

    return out


def part1():
    shapes, regions = getInput()

    shape_orients = []
    for sh in shapes:
        shape_orients.append(get_orientations(sh))

    ok_regions = 0

    for region_line in regions:
        W, H, counts = parseRegion(region_line)

        region_area = W * H
        need_cells = 0
        for si in range(len(counts)):
            shape_size = len(shape_orients[si][0])
            need_cells += counts[si] * shape_size
        if need_cells > region_area:
            continue

        pieces = []
        for si, cnt in enumerate(counts):
            for _ in range(cnt):
                pieces.append(si)

        pieces.sort(key=lambda si: -len(shape_orients[si][0]))

        filled = []
        for _ in range(H):
            filled.append([False] * W)

        memo = set()

        def encode_state(i):
            bits = []
            for r in range(H):
                for c in range(W):
                    bits.append('1' if filled[r][c] else '0')
            return str(i) + "|" + "".join(bits)

        def free_cells_count():
            cnt = 0
            for r in range(H):
                for c in range(W):
                    if not filled[r][c]:
                        cnt += 1
            return cnt

        def remaining_cells_needed(i):
            total = 0
            for k in range(i, len(pieces)):
                total += len(shape_orients[pieces[k]][0])
            return total

        def can_place(cells, top_r, top_c):
            for dr, dc in cells:
                rr = top_r + dr
                cc = top_c + dc
                if rr < 0 or rr >= H or cc < 0 or cc >= W:
                    return False
                if filled[rr][cc]:
                    return False
            return True

        def do_place(cells, top_r, top_c, val):
            for dr, dc in cells:
                filled[top_r + dr][top_c + dc] = val

        def solve(i):
            if i == len(pieces):
                return True

            # prune: not enough free space left to place remaining pieces
            if remaining_cells_needed(i) > free_cells_count():
                return False

            key = encode_state(i)
            if key in memo:
                return False
            memo.add(key)

            shape_index = pieces[i]

            for orient in shape_orients[shape_index]:
                max_r = 0
                max_c = 0
                for dr, dc in orient:
                    if dr > max_r:
                        max_r = dr
                    if dc > max_c:
                        max_c = dc

                for top_r in range(H - max_r):
                    for top_c in range(W - max_c):
                        if can_place(orient, top_r, top_c):
                            do_place(orient, top_r, top_c, True)
                            if solve(i + 1):
                                return True
                            do_place(orient, top_r, top_c, False)

            return False

        if solve(0):
            ok_regions += 1

    print(ok_regions)


if __name__ == "__main__":
    part1()
