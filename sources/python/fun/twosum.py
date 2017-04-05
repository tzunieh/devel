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

def leetcode_twosum(data, sum):
    sorted_data = sorted(data + [sum])
    sorted_data = sorted_data[0:sorted_data.index(sum)]

    for value in sorted_data:
        try:
            idx_0 = data.index(sum - value)
            idx_1 = data.index(value)
            return [idx_0, idx_1] if idx_0 < idx_1 else [idx_1, idx_0]
        except:
            continue


class TestStringMethods(unittest.TestCase):

    def test_sorted_twosum(self):
        self.assertEqual(
            leetcode_twosum([2, 7, 11, 15], 9), 
            [0, 1]
        )
        self.assertEqual(
            leetcode_twosum([2, 7, 11, 15], 18), 
            [1, 2]
        )

    def test_unsorted_twosum(self):
        self.assertEqual(
            leetcode_twosum([3, 2, 9, 11, 7, 4], 5), 
            [0, 1]
        )
        self.assertEqual(
            leetcode_twosum([3, 2, 9, 11, 7, 4], 20), 
            [2, 3]
        )
        self.assertEqual(
            leetcode_twosum([3, 22, 9, 11, 7, 4], 15), 
            [3, 5]
        )

if __name__ == '__main__':
    unittest.main()