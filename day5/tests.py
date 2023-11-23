import unittest
from impl import process


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(process(1, "sample.txt"), "CMZ")

    def test_part1_input(self):
        self.assertEqual(process(1, "input.txt"), "FCVRLMVQP")

    def test_part2_sample(self):
        self.assertEqual(process(2, "sample.txt"), "MCD")

    def test_part2_input(self):
        self.assertEqual(process(2, "input.txt"), "RWLWGJGFD")


if __name__ == '__main__':
    unittest.main()
