# coding=utf-8
import unittest

"""7. Reverse Integer
https://leetcode.com/problems/reverse-integer/description/

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

    
    
    **Input:** 123
    **Output:** 321
    

**Example 2:**

    
    
    **Input:** -123
    **Output:** -321
    

**Example 3:**

    
    
    **Input:** 120
    **Output:** 21
    

**Note:**  
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [ −2^31,  2^31 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.


Similar Questions:
  String to Integer (atoi) (string-to-integer-atoi)
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = -x

        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
