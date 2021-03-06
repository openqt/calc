# coding=utf-8
import unittest

"""136. Single Number
https://leetcode.com/problems/single-number/description/

Given a **non-empty**  array of integers, every element appears _twice_ except
for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

**Example 1:**

    
    
    **Input:** [2,2,1]
    **Output:** 1
    

**Example 2:**

    
    
    **Input:** [4,1,2,1,2]
    **Output:** 4


Similar Questions:
  Single Number II (single-number-ii)
  Single Number III (single-number-iii)
  Missing Number (missing-number)
  Find the Duplicate Number (find-the-duplicate-number)
  Find the Difference (find-the-difference)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = set()
        for i in nums:
            if i in val:
                val.remove(i)
            else:
                val.add(i)
        return val.pop()


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.singleNumber([2, 2, 1]), 1)
        self.assertEqual(s.singleNumber([4, 1, 2, 1, 2]), 4)


if __name__ == "__main__":
    unittest.main()
