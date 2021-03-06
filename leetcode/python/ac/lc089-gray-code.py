# coding=utf-8
import unittest

"""89. Gray Code
https://leetcode.com/problems/gray-code/description/

The gray code is a binary numeral system where two successive values differ in
only one bit.

Given a non-negative integer _n_ representing the total number of bits in the
code, print the sequence of gray code. A gray code sequence must begin with 0.

**Example 1:**

    
    
    **Input:**  2
    **Output:**  [0,1,3,2]
    **Explanation:**
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
    For a given   _n_ , a gray code sequence may not be uniquely defined.
    For example, [0,2,3,1] is also a valid gray code sequence.
    
    00 - 0
    10 - 2
    11 - 3
    01 - 1
    

**Example 2:**

    
    
    **Input:**  0
    **Output:**  [0]
    **Explanation:** We define the gray code sequence to begin with 0.
                  A gray code sequence of _n_ has size = 2 n, which for _n_ = 0 the size is 2 0 = 1.
                 Therefore, for _n_ = 0 the gray code sequence is [0].


Similar Questions:
  1-bit and 2-bit Characters (1-bit-and-2-bit-characters)
"""


class Solution(object):
    def grayCode1(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        code = [0]
        for i in range(n):
            mask = 1 << i
            code.extend([i | mask for i in code[::-1]])
        return code

    def grayCode(self, n):
        """Gray码的第n个数（从0算起）是n xor (n shr 1)
        :type n: int
        :rtype: List[int]
        """
        code = []
        for i in range(2 ** n):
            code.append(i ^ (i >> 1))
        return code


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.grayCode(0), [0])
        self.assertEqual(s.grayCode(2), [0, 1, 3, 2])
        self.assertEqual(s.grayCode(3), [0, 1, 3, 2, 6, 7, 5, 4])


if __name__ == "__main__":
    unittest.main()
