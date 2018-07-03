# coding=utf-8
import unittest

"""762. Prime Number of Set Bits in Binary Representation
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

Given two integers `L` and `R`, find the count of numbers in the range `[L,
R]` (inclusive) having a prime number of set bits in their binary
representation.

(Recall that the number of set bits an integer has is the number of `1`s
present when written in binary. For example, `21` written in binary is `10101`
which has 3 set bits. Also, 1 is not a prime.)

**Example 1:**  

    
    
    **Input:** L = 6, R = 10
    **Output:** 4
    **Explanation:**
    6 -> 110 (2 set bits, 2 is prime)
    7 -> 111 (3 set bits, 3 is prime)
    9 -> 1001 (2 set bits , 2 is prime)
    10->1010 (2 set bits , 2 is prime)
    

**Example 2:**  

    
    
    **Input:** L = 10, R = 15
    **Output:** 5
    **Explanation:**
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)
    

**Note:**  

  1. `L, R` will be integers `L <= R` in the range `[1, 10^6]`.
  2. `R - L` will be at most 10000.


Similar Questions:
  Number of 1 Bits (number-of-1-bits)
"""


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()