from functools import reduce
import math

#  ─────────────────────────── Brute Force ──────────────────────────


def check_repeat(s: str, r: int) -> bool:
    """
    Check if the number has `r` length of repeated patterns.
    E.g.
    if n = 123123 and r = 3 => 123 and 123 are repeated patterns of length 3.
    if n = 123123 and r = 2 => 12 31 23 are not repeated patterns of length 3.
    """
    if r > (len(s) / 2) or len(s) % r > 0:  # cannot be equally divided
        return False

    # Break down string into parts of `r` length
    num_parts = int(len(s) / r)
    parts = []
    for i in range(num_parts):
        start = i * r
        end = (i + 1) * r
        parts.append(s[start:end])

    # Check all parts are same
    base = parts[0]
    for i in range(1, len(parts)):
        if parts[i] != base:
            return False

    return True


def invalid_id_V2(n: int) -> bool:
    s = str(n)
    max_r = int(math.ceil(len(s) / 2))

    for r in range(1, max_r + 1):
        if check_repeat(s, r):
            return True

    return False


def invalid_id(n: int) -> bool:
    """
    Given a number `n` check if it is made up of just repeating numbers.
    """
    s = str(n)
    # If len is odd, then it cannot be repeating number
    if len(s) % 2 == 1:
        return False

    mid = int(len(s) / 2)
    return check_repeat(s, mid)


def find_invalid(ranges: list[tuple[int, int]]) -> int:
    """
    Go through each range - find the invalid nums and add them.
    """
    ans = 0
    for start, end in ranges:
        print(f"Working on range: {start} - {end}")
        for n in range(start, end+1):
            print(f"Testing {n}", end='\r')
            if invalid_id_V2(n):
                ans += n
    return ans


#  ────────────────────────── Util function ─────────────────────────


def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def get_range(line: str) -> tuple[int, int]:
    start, end = line.split('-')
    return (int(start), int(end))


if __name__ == "__main__":
    puzzle_input = "12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
    # puzzle_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    ranges = [i for i in map(get_range, puzzle_input.split(","))]

    total_nums_to_evaluate = reduce(lambda acc, x: acc + x,
                                    map(lambda x: x[1] - x[0], ranges))
    print(f"Total nums to evaluate: {total_nums_to_evaluate}")

    ans = find_invalid(ranges)
    print(f"Answer: {ans}")
