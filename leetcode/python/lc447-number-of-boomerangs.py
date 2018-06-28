# coding=utf-8
import unittest

"""447. Number of Boomerangs
https://leetcode.com/problems/number-of-boomerangs/description/

Given _n_ points in the plane that are all pairwise distinct, a "boomerang" is
a tuple of points `(i, j, k)` such that the distance between `i` and `j`
equals the distance between `i` and `k` ( **the order of the tuple matters**
).

Find the number of boomerangs. You may assume that _n_ will be at most **500**
and coordinates of points are all in the range **[-10000, 10000]**
(inclusive).

**Example:**  

    
    
    **Input:**
    [[0,0],[1,0],[2,0]]
    
    **Output:**
    2
    
    **Explanation:**
    The two boomerangs are **[[1,0],[0,0],[2,0]]** and **[[1,0],[2,0],[0,0]]**


Similar Questions:
  Line Reflection (line-reflection)
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
