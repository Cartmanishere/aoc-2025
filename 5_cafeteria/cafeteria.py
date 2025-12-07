#  ────────────────────────── Hard version ──────────────────────────

def merge(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """
    For given two ranges, check if they overlap and if so - give a merged range
    """
    s1, e1 = r1
    s2, e2 = r2

    if s1 > s2 and e2 >= s1:
        return (s2, max(e1, e2))

    if s2 >= s1 and e1 >= s2:
        return (s1, max(e1, e2))


def merge_overlapping(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merge overlapping ranges to generate a single range
    """
    # Consider all ranges with each other in a bubble sort kind of way
    already_merged = set()
    for i in range(len(ranges) - 1):
        # short circuit if range was already merged
        if i in already_merged:
            continue

        for j in range(i + 1, len(ranges)):
            # short circuit if range was already merged
            if j in already_merged:
                continue

            r1, r2 = ranges[i], ranges[j]
            merged_range = merge(r1, r2)

            if merged_range is not None:
                ranges[j] = merged_range
                already_merged.add(i)

    return map(
        lambda x: ranges[x],
        # consider only those indices whose ranges didn't get merged
        filter(lambda x: x not in already_merged, range(len(ranges)))
    )


def count_all_fresh(ranges: list[tuple[int, int]]) -> int:
    """
    Based on analysis - number of ranges is small.
    """
    merged_ranges = merge_overlapping(ranges)
    total_ids = 0
    for start, end in merged_ranges:
        total_ids += (end - start) + 1  # because inclusive
    return total_ids

#  ────────────────────────── Easy version ──────────────────────────


def check_fresh(ranges: list[tuple[int, int]], id: int) -> bool:
    for start, end in ranges:
        if id >= start and id <= end:
            return True
    return False


def count_fresh_ids(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    return len(list(filter(lambda x: check_fresh(ranges, x), ids)))


#  ────────────────────────── Util function ─────────────────────────

def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))


def get_range(line: str) -> tuple[int, int]:
    start, end = line.split('-')
    return (int(start), int(end))


def form_input(lines: str) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Takes input file and returns two lists.
    First list is a list of ranges
    Second list is a list of ingredient ids.
    """
    ranges = []
    idx = 0
    while True:
        if lines[idx] == '':
            break
        ranges.append(get_range(lines[idx]))
        idx += 1

    ids = list(map(lambda x: int(x), lines[idx + 1:]))
    return (ranges, ids)


if __name__ == "__main__":
    lines = read_file('input.txt')
    ranges, ids = form_input(lines)

    #  ──────────────────────── Analyze input ───────────────────────
    print(f"Number of ranges: {len(ranges)}")
    print(f"Number of ids: {len(ids)}")
    total_range_cover = 0
    for start, end in ranges:
        total_range_cover += (end - start)
    print(f"Total range cover: {total_range_cover}")

    #  ─────────────────────────── Sample ───────────────────────────
    sample_lines = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()
    sample_ranges, sample_ids = form_input(sample_lines)
    sample_ans = count_fresh_ids(sample_ranges, sample_ids)
    print(f"Sample Answer: {sample_ans}")

    #  ──────────────────────── Easy version ────────────────────────
    ans = count_fresh_ids(ranges, ids)
    print(f"V1 Answer: {ans}")

    #  ──────────────────────── Hard version ────────────────────────
    merged_ranges = merge_overlapping(ranges)
    # print(f"Merged ranges: {merged_ranges}")
    ans = count_all_fresh(ranges)
    print(f"V2 Answer: {ans}")
