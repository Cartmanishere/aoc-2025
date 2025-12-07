import unittest
from forklift import make_grid, find_accessible_rolls, with_roll_removal


class TestForklift(unittest.TestCase):
    sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    def test_find_accessible_rolls(self):
        #  ──────────────────────── Sample input ────────────────────────
        sample_grid = make_grid(self.sample.splitlines())
        print("Sample grid:")
        for i in sample_grid:
            print(i)
        sample_ans = find_accessible_rolls(sample_grid)
        self.assertEqual(sample_ans, 13)

    def test_with_removable_rolls(self):
        sample_grid = make_grid(self.sample.splitlines())
        print("Sample grid:")
        for i in sample_grid:
            print(i)
        sample_ans = with_roll_removal(sample_grid)
        self.assertEqual(sample_ans, 43)


if __name__ == '__main__':
    unittest.main()
