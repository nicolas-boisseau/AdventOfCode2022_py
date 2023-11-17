import unittest
from day1 import process


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(process(1, "sample.txt"), 24000)

    def test_part1_input(self):
        self.assertEqual(process(1, "input.txt"), 67016)

    def test_part2_sample(self):
        self.assertEqual(process(2, "sample.txt"), 45000)

    def test_part2_input(self):
        self.assertEqual(process(2, "input.txt"), 200116)


if __name__ == '__main__':
    unittest.main()
