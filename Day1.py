# This implementation assumes an always correct input

def part1():
    MOD = 100  # dial has positions 0..99
    pos = 50  # starting position
    count_zero = 0 # how many times we land on zero
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()

            direction = line[0]
            steps = int(line[1:])

            if direction == 'R':
                pos = (pos + steps) % MOD
            else:
                pos = (pos - steps) % MOD

            if pos == 0:
                count_zero += 1

    print(count_zero)

def part2():
    MOD = 100  # dial has positions 0..99
    pos = 50  # starting position
    zero_clicks = 0  # how many times any click lands on 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            steps = int(line[1:])

            # Count how many times we hit 0 DURING this rotation
            if direction == 'R':
                # pos + k ≡ 0 (mod 100) -> k ≡ -pos (mod 100)
                residue = (-pos) % MOD
            else:  # 'L'
                # pos - k ≡ 0 (mod 100) -> k ≡ pos (mod 100)
                residue = pos % MOD

            # First positive k where we land on 0
            first_k = residue if residue != 0 else MOD  # skip k=0 (starting position)

            if first_k <= steps:
                zero_clicks += 1 + (steps - first_k) // MOD

            # Now actually perform the rotation to update pos
            if direction == 'R':
                pos = (pos + steps) % MOD
            else:  # 'L'
                pos = (pos - steps) % MOD

    print(zero_clicks)

if __name__ == "__main__":
    part1()
    part2()
