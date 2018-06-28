# coding=utf-8
import unittest

"""402. Remove K Digits
https://leetcode.com/problems/remove-k-digits/description/

Given a non-negative integer _num_ represented as a string, remove _k_ digits
from the number so that the new number is the smallest possible.

**Note:**  

  * The length of _num_ is less than 10002 and will be  ≥ _k_.
  * The given _num_ does not contain any leading zero.

**

**Example 1:**

    
    
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    

**Example 2:**

    
    
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
    

**Example 3:**

    
    
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Similar Questions:
  Create Maximum Number (create-maximum-number)
  Monotone Increasing Digits (monotone-increasing-digits)
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
