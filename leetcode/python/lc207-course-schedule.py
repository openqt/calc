# coding=utf-8
import unittest

"""207. Course Schedule
https://leetcode.com/problems/course-schedule/description/

There are a total of _n_ courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs** , is it
possible for you to finish all courses?

**Example 1:**

    
    
    **Input:** 2, [[1,0]] 
    **Output:** true
    **Explanation:**  There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

    
    
    **Input:** 2, [[1,0],[0,1]]
    **Output:** false
    **Explanation:**  There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.
    

**Note:**

  1. The input prerequisites is a graph represented by **a list of edges** , not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
  2. You may assume that there are no duplicate edges in the input prerequisites.


Similar Questions:
  Course Schedule II (course-schedule-ii)
  Graph Valid Tree (graph-valid-tree)
  Minimum Height Trees (minimum-height-trees)
  Course Schedule III (course-schedule-iii)
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
