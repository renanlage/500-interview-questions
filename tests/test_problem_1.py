from unittest.case import TestCase
from problems.problem_1 import naive_pair_with_sum, ordered_pair_with_sum, hash_pair_with_sum


class Problem1Test(TestCase):
    def test_pair_with_sum_return_pair_whose_sum_is_sum(self):
        arr = [8, 7, 2, 5, 3, 1]
        self.assertEqual(sum(arr[i] for i in naive_pair_with_sum(arr, 10)), 10)
        self.assertEqual(sum(arr[i] for i in naive_pair_with_sum(arr, 9)), 9)
        self.assertEqual(sum(arr[i] for i in naive_pair_with_sum(arr, 8)), 8)

    def test_pair_with_sum_return_none_if_no_pair_found(self):
        self.assertEqual(naive_pair_with_sum([], 10), None)
        self.assertEqual(ordered_pair_with_sum([6], 10), None)
        self.assertEqual(naive_pair_with_sum([8, 7, 2, 5, 3, 1], 100), None)

    def test_ordered_pair_with_sum_return_pair_whose_sum_is_sum(self):
        arr = [8, 7, 2, 5, 3, 1]
        self.assertEqual(sum(arr[i] for i in ordered_pair_with_sum(arr, 10)), 10)
        self.assertEqual(sum(arr[i] for i in ordered_pair_with_sum(arr, 9)), 9)
        self.assertEqual(sum(arr[i] for i in ordered_pair_with_sum(arr, 8)), 8)

    def test_ordered_pair_with_sum_return_none_if_no_pair_found(self):
        self.assertEqual(ordered_pair_with_sum([], 10), None)
        self.assertEqual(ordered_pair_with_sum([6], 10), None)
        self.assertEqual(ordered_pair_with_sum([8, 7, 2, 5, 3, 1], 100), None)

    def test_hash_pair_with_sum_return_pair_whose_sum_is_sum(self):
        arr = [8, 7, 2, 5, 3, 1]
        self.assertEqual(sum(arr[i] for i in hash_pair_with_sum(arr, 10)), 10)
        self.assertEqual(sum(arr[i] for i in hash_pair_with_sum(arr, 9)), 9)
        self.assertEqual(sum(arr[i] for i in hash_pair_with_sum(arr, 8)), 8)

    def test_hash_pair_with_sum_return_none_if_no_pair_found(self):
        self.assertEqual(hash_pair_with_sum([], 10), None)
        self.assertEqual(hash_pair_with_sum([6], 10), None)
        self.assertEqual(hash_pair_with_sum([8, 7, 2, 5, 3, 1], 100), None)
