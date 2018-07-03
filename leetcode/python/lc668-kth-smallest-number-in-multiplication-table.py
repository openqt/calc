# coding=utf-8
import unittest

"""668. Kth Smallest Number in Multiplication Table
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/

Nearly every one have used the [Multiplication
Table](https://en.wikipedia.org/wiki/Multiplication_table). But could you find
out the `k-th` smallest number quickly from the multiplication table?

Given the height `m` and the length `n` of a `m * n` Multiplication Table, and
a positive integer `k`, you need to return the `k-th` smallest number in this
table.

**Example 1:**  

    
    
    **Input:** m = 3, n = 3, k = 5
    **Output:** 
    **Explanation:** 
    The Multiplication Table:
    1	2	3
    2	4	6
    3	6	9
    
    The 5-th smallest number is 3 (1, 2, 2, 3, 3).
    

**Example 2:**  

    
    
    **Input:** m = 2, n = 3, k = 6
    **Output:** 
    **Explanation:** 
    The Multiplication Table:
    1	2	3
    2	4	6
    
    The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
    

**Note:**  

  1. The `m` and `n` will be in the range [1, 30000].
  2. The `k` will be in the range [1, m * n]


Similar Questions:
  Kth Smallest Element in a Sorted Matrix (kth-smallest-element-in-a-sorted-matrix)
  Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
  K-th Smallest Prime Fraction (k-th-smallest-prime-fraction)
"""


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()