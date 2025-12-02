import bisect

def part1():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    # Split on commas
    parts = [p for p in line.split(",") if p]

    ranges = []
    for p in parts:
        start_str, end_str = p.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

    # Find the largest upper bound to know how far to generate invalid IDs
    max_end = max(end for (_, end) in ranges)
    max_len = len(str(max_end))

    # Generate all "double-pattern" numbers up to max_end
    invalid_ids = []

    for total_len in range(2, max_len + 1, 2):  # only even lengths
        half_len = total_len // 2
        start_x = 10 ** (half_len - 1)          # no leading zeros
        end_x = 10 ** half_len - 1

        base = 10 ** half_len  # used for numeric construction

        for x in range(start_x, end_x + 1):
            n = x * base + x
            if n > max_end:
                break
            invalid_ids.append(n)

    invalid_ids.sort()

    # Build prefix sums so we can sum ranges in O(1)
    prefix = [0]
    for n in invalid_ids:
        prefix.append(prefix[-1] + n)

    def sum_in_range(lo_val, hi_val):
        """Sum invalid_ids that are between lo_val and hi_val inclusive."""
        left = bisect.bisect_left(invalid_ids, lo_val)
        right = bisect.bisect_right(invalid_ids, hi_val)
        return prefix[right] - prefix[left]

    # Sum for all ranges
    total = 0
    for start, end in ranges:
        total += sum_in_range(start, end)

    print(total)





def generate_invalid_ids(max_end):

    max_len = len(str(max_end))
    invalid_ids = set()

    for base_len in range(1, max_len + 1):
        t_max = max_len // base_len
        if t_max < 2:
            continue  # cant repeat at least twice

        start_x = 10 ** (base_len - 1)      # no leading zeros
        end_x = 10 ** base_len - 1
        power = 10 ** base_len              # used for numeric concatenation

        for x in range(start_x, end_x + 1):
            v = x
            for t in range(2, t_max + 1):
                # v becomes x repeated t times
                v = v * power + x
                total_len = base_len * t

                if total_len < max_len:
                    # Any number with fewer digits than max_end is <= max_end
                    invalid_ids.add(v)
                elif total_len == max_len:
                    if v <= max_end:
                        invalid_ids.add(v)
                else:
                    break

    return sorted(invalid_ids)


def sum_invalid_in_ranges(ranges, invalid_ids):
    prefix = [0]
    for n in invalid_ids:
        prefix.append(prefix[-1] + n)

    def sum_in_range(lo, hi):
        left = bisect.bisect_left(invalid_ids, lo)
        right = bisect.bisect_right(invalid_ids, hi)
        return prefix[right] - prefix[left]

    total = 0
    for start, end in ranges:
        total += sum_in_range(start, end)
    return total


def part2():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    # Split on commas
    parts = [p for p in line.split(",") if p]

    ranges = []
    for p in parts:
        start_str, end_str = p.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

    max_end = max(end for _, end in ranges)

    invalid_ids = generate_invalid_ids(max_end)
    total = sum_invalid_in_ranges(ranges, invalid_ids)

    print(total)


if __name__ == "__main__":
    part1()
    part2()