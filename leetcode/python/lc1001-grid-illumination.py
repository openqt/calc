# coding=utf-8
import unittest

"""1001. Grid Illumination
https://leetcode.com/problems/grid-illumination/description/

On a `N x N` grid of cells, each cell `(x, y)` with `0 <= x < N` and `0 <= y <
N` has a lamp.

Initially, some number of lamps are on.  `lamps[i]` tells us the location of
the `i`-th lamp that is on.  Each lamp that is on illuminates every square on
its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query `queries[i] = (x, y)`, the answer to the query is 1 if the
cell (x, y) is illuminated, else 0.

After each query `(x, y)` [in the order given by `queries`], we turn off any
lamps that are at cell `(x, y)` or are adjacent 8-directionally (ie., share a
corner or edge with cell `(x, y)`.)

Return an array of answers.  Each value `answer[i]` should be equal to the
answer of the `i`-th query `queries[i]`.



**Example 1:**

    
    
    **Input:** N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
    **Output:** [1,0]
    **Explanation:**
    Before performing the first query we have both lamps [0,0] and [4,4] on.
    The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
    1 1 1 1 1
    1 1 0 0 1
    1 0 1 0 1
    1 0 0 1 1
    1 1 1 1 1
    Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
    1 0 0 0 1
    0 1 0 0 1
    0 0 1 0 1
    0 0 0 1 1
    1 1 1 1 1
    Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
    



**Note:**

  1. `1 <= N <= 10^9`
  2. `0 <= lamps.length <= 20000`
  3. `0 <= queries.length <= 20000`
  4. `lamps[i].length == queries[i].length == 2`


Similar Questions:

"""


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
