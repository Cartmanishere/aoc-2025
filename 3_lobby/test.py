import unittest
from lobby import find_max_joltage_v2


class TestFindMaxJoltageV2(unittest.TestCase):

    def test_find_max_joltage_v2(self):
        self.assertEqual(find_max_joltage_v2("987654321111111"), 987654321111)
        self.assertEqual(find_max_joltage_v2("811111111111119"), 811111111119)
        self.assertEqual(find_max_joltage_v2("234234234234278"), 434234234278)
        self.assertEqual(find_max_joltage_v2("818181911112111"), 888911112111)


if __name__ == '__main__':
    unittest.main()
