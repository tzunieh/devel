"""
Source: https://leetcode.com/problems/two-sum/#/description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
import unittest

def twosum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for idx_0, val_0 in enumerate(nums):
        try:
            idx_1 = nums[(idx_0 + 1):].index(target - val_0)
            return [idx_0, idx_1 + idx_0 + 1]
        except:
            continue
        

class TestStringMethods(unittest.TestCase):

    def test_sorted_twosum(self):
        self.assertEqual(
            twosum([2, 7, 11, 15], 9),
            [0, 1]
        )
        self.assertEqual(
            twosum([2, 7, 11, 15], 18),
            [1, 2]
        )

    def test_unsorted_twosum(self):
        self.assertEqual(
            twosum([3, 2, 9, 11, 7, 4], 5),
            [0, 1]
        )
        self.assertEqual(
            twosum([3, 2, 9, 11, 7, 4], 20),
            [2, 3]
        )
        self.assertEqual(
            twosum([3, 22, 9, 11, 7, 4], 15),
            [3, 5]
        )

    def test_duplicated_twosum(self):
        self.assertEqual(
            twosum([3, 3, 5, 7, 9], 6),
            [0, 1]
        )

    def test_zero_twosum(self):
        self.assertEqual(
            twosum([0, 4, 3, 0], 0),
            [0, 3]
        )

    def test_negative_twosum(self):
        self.assertEqual(
            twosum([0, 4, 3, -2], 2),
            [1, 3]
        )


if __name__ == '__main__':
    unittest.main()
