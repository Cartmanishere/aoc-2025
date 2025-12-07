def find_max_with_index(s: str) -> tuple[int, int]:
    """
    Returns the max value in the string of numbers along with its index.
    E.g (idx, int)
    Note: Only find the first max idx.
    """
    m = 0
    midx = -1
    for idx, num in enumerate(s):
        n = int(num)
        if n > m:
            midx = idx
            m = n
    return (midx, m)


def substr(s: str, start: int, end: int) -> str:
    """
    Because python list/str substr syntax s[x:y] does not support 0 for y.
    """
    if end == 0:
        return s[start:]
    else:
        return s[start:end]

#  ────────────────────────── Hard version ──────────────────────────


def find_max_joltage_v2(bank: str) -> int:

    # init
    joltage_str = ''
    sidx = -1

    # main loop
    for i in range(12, 0, -1):
        check_bank = substr(bank, sidx + 1, (i * -1) + 1)
        fidx, fnum = find_max_with_index(check_bank)

        sidx += fidx + 1
        joltage_str += str(fnum)

    # return
    return int(joltage_str)


def total_joltage_v2(banks: list[str]) -> int:
    total = 0
    for bank in banks:
        total += find_max_joltage_v2(bank)
    return total

#  ───────────────────────── Easier version ─────────────────────────


def find_max_joltage(bank: str) -> int:
    """
    Given a battery bank - find the max possible joltage.
    """
    # Logic
    # Find the max value between 0 - n-1 of the string.
    # Suppose the max value is present at i
    # Find the max  value between i to n of the string.
    fidx, fnum = find_max_with_index(bank[:-1])
    sidx, snum = find_max_with_index(bank[fidx+1:])
    return int(f"{fnum}{snum}")


def total_joltage(banks: list[str]) -> int:
    total = 0
    for bank in banks:
        total += find_max_joltage(bank)
    return total

#  ────────────────────────── Util function ─────────────────────────


def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return map(lambda x: x.replace('\n', ''), lines)


if __name__ == "__main__":
    banks = list(read_file('input.txt'))

    ans = total_joltage(banks)
    print(f"V1 Answer {ans}")

    ans = total_joltage_v2(banks)
    print(f"V2 Answer {ans}")
