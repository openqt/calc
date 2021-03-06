import unittest

"""695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/

Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
     
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
    [[0,0,0,0,0,0,0,0]]

    Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution(unittest.TestCase):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] > 0:
                grid[x][y] = 0
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
            return 0

        val = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                val = max(val, dfs(x, y))
        return val

    def test(self):
        self.assertEqual(self.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]), 6)
        self.assertEqual(self.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]), 0)
        self.assertEqual(self.maxAreaOfIsland([[1]]), 1)
        self.assertEqual(self.maxAreaOfIsland([[1, 1],
                                               [1, 0]]), 3)
        self.assertEqual(self.maxAreaOfIsland([[1, 1, 0, 1, 1],
                                               [1, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 1],
                                               [1, 1, 0, 1, 1]]), 3)
        self.assertEqual(self.maxAreaOfIsland([[1, 1, 0, 0, 0],
                                               [1, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 1],
                                               [0, 0, 0, 1, 1]]), 4)
        self.assertEqual(self.maxAreaOfIsland([[0, 1],
                                               [1, 0]]), 1)


if __name__ == "__main__":
    unittest.main()
