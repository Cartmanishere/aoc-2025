def gen_grid_traverse(grid: list[list[str]]):
    len_y = len(grid[0])
    len_x = len(grid)
    for i in range(len_x):
        for j in range(len_y):
            yield (i, j)


def gen_adjacent(grid: list[list[str]], x: int, y: int):
    """
    For each grid point, there should be at max 8 adjacent points.
    This function generates the adjacent for any given grid point.
    Let's call all adjacent as
    1. top
    2. top-left
    3. top-right
    4. bottom
    7. bottom-left
    8. bottom-right
    2. left
    3. right
    Note: x represent vertical column, while y represents horizontal column.
    """
    grid_y = len(grid[0])
    grid_x = len(grid)
    assert x < grid_x and y < grid_y, "This should not happen"
    # check top exists
    if x - 1 >= 0:
        yield (x - 1, y)

    # check bottom exists
    if x + 1 < grid_x:
        yield (x + 1, y)

    # check left exists
    if y - 1 >= 0:
        yield (x, y - 1)

    # check right exists
    if y + 1 < grid_y:
        yield (x, y + 1)

    # check top-left exists
    if x - 1 >= 0 and y - 1 >= 0:
        yield (x - 1, y - 1)

    # check top-right exists
    if x - 1 >= 0 and y + 1 < grid_y:
        yield (x - 1, y + 1)

    # check bottom-left exists
    if x + 1 < grid_x and y - 1 >= 0:
        yield (x + 1, y - 1)

    # check bottom-right exists
    if x + 1 < grid_x and y + 1 < grid_y:
        yield (x + 1, y + 1)


def gen_accessible_rolls(grid: list[list[str]]):
    for grid_point in gen_grid_traverse(grid):
        adjancent_rolls = 0
        # Skip check if there isn't a roll at this point
        if grid[grid_point[0]][grid_point[1]] != '@':
            continue

        for adjacent_point in gen_adjacent(grid, grid_point[0], grid_point[1]):
            if grid[adjacent_point[0]][adjacent_point[1]] == '@':
                adjancent_rolls += 1

        if adjancent_rolls < 4:
            yield grid_point


#  ───────────────────────── Harder version ─────────────────────────

def remove_rolls(grid: list[list[str]], rolls_to_remove: list[tuple[int, int]]):
    for (x, y) in rolls_to_remove:
        grid[x][y] = '.'


def with_roll_removal(grid: list[list[str]]) -> int:
    total_removed_rolls = 0
    while True:
        rolls_to_remove = list(gen_accessible_rolls(grid))

        if len(rolls_to_remove) == 0:
            break

        total_removed_rolls += len(rolls_to_remove)
        remove_rolls(grid, rolls_to_remove)

    return total_removed_rolls


#  ───────────────────────── Easier version ─────────────────────────

def find_accessible_rolls(grid: list[list[str]]) -> int:
    accessible_rolls = 0
    for grid_point in gen_grid_traverse(grid):
        adjancent_rolls = 0
        # Skip check if there isn't a roll at this point
        if grid[grid_point[0]][grid_point[1]] != '@':
            continue

        for adjacent_point in gen_adjacent(grid, grid_point[0], grid_point[1]):
            if grid[adjacent_point[0]][adjacent_point[1]] == '@':
                adjancent_rolls += 1
        if adjancent_rolls < 4:
            accessible_rolls += 1
    return accessible_rolls


#  ────────────────────────── Util function ─────────────────────────

def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def make_grid(lines: list[str]) -> list[list[str]]:
    return [[i for i in line] for line in lines]


if __name__ == "__main__":
    lines = read_file('input.txt')
    paper_grid = make_grid(lines)
    #  ───────────────────────── Easy answer ────────────────────────
    ans = find_accessible_rolls(paper_grid)
    print(f"V1 Answer: {ans}")

    #  ───────────────────────── Hard answer ────────────────────────
    ans = with_roll_removal(paper_grid)
    print(f"V2 Answer: {ans}")
