# coding=utf-8
import unittest

"""210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/description/

There are a total of _n_ courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs** ,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If
it is impossible to finish all courses, return an empty array.

**Example 1:**

    
    
    **Input:** 2, [[1,0]] 
    **Output:**[0,1]
    **Explanation:**  There are a total of 2 courses to take. To take course 1 you should have finished   
                 course 0. So the correct course order is [0,1] .

**Example 2:**

    
    
    **Input:** 4, [[1,0],[2,0],[3,1],[3,2]]
    **Output:**[0,1,2,3] or [0,2,1,3]
    **Explanation:**  There are a total of 4 courses to take. To take course 3 you should have finished both     
                 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

**Note:**

  1. The input prerequisites is a graph represented by **a list of edges** , not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
  2. You may assume that there are no duplicate edges in the input prerequisites.


Similar Questions:
  Course Schedule (course-schedule)
  Alien Dictionary (alien-dictionary)
  Minimum Height Trees (minimum-height-trees)
  Sequence Reconstruction (sequence-reconstruction)
  Course Schedule III (course-schedule-iii)
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
