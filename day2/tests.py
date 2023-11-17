import unittest
from code import process


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(process(1, "sample.txt"), 15)

    def test_part1_input(self):
        self.assertEqual(process(1, "input.txt"), 11150)

    def test_part2_sample(self):
        self.assertEqual(process(2, "sample.txt"), 12)

    def test_part2_input(self):
        self.assertEqual(process(2, "input.txt"), 8295)


if __name__ == '__main__':
    unittest.main()
