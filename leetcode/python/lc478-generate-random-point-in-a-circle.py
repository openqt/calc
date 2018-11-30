# coding=utf-8
import unittest

"""478. Generate Random Point in a Circle
https://leetcode.com/problems/generate-random-point-in-a-circle/description/

Given the radius and x-y positions of the center of a circle, write a function
`randPoint` which generates a uniform random point in the circle.

Note:

  1. input and output values are in [floating-point](https://www.webopedia.com/TERM/F/floating_point_number.html).
  2. radius and x-y position of the center of the circle is passed into the class constructor.
  3. a point on the circumference of the circle is considered to be in the circle.
  4. `randPoint` returns a size 2 array containing x-position and y-position of the random point, in that order.

**Example 1:**

    
    
    **Input:** ["Solution","randPoint","randPoint","randPoint"]
    [[1,0,0],[],[],[]]
    **Output:** [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
    

**Example 2:**

    
    
    **Input:** ["Solution","randPoint","randPoint","randPoint"]
    [[10,5,-7.5],[],[],[]]
    **Output:** [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments.
`Solution`'s constructor has three arguments, the radius, x-position of the
center, and y-position of the center of the circle. `randPoint` has no
arguments. Arguments are always wrapped with a list, even if there aren't any.


Similar Questions:
  Random Point in Non-overlapping Rectangles (random-point-in-non-overlapping-rectangles)
"""


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
