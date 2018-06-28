# coding=utf-8
import unittest

"""837. New 21 Game
https://leetcode.com/problems/new-21-game/description/

Alice plays the following game, loosely based on the card game "21".

Alice starts with `0` points, and draws numbers while she has less than `K`
points.  During each draw, she gains an integer number of points randomly from
the range `[1, W]`, where `W` is an integer.  Each draw is independent and the
outcomes have equal probabilities.

Alice stops drawing numbers when she gets `K` or more points.  What is the
probability that she has `N` or less points?

**Example 1:**

    
    
    **Input:** N = 10, K = 1, W = 10
    **Output:** 1.00000
    **Explanation:** Alice gets a single card, then stops.
    

**Example 2:**

    
    
    **Input:** N = 6, K = 1, W = 10
    **Output:** 0.60000
    **Explanation:** Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.
    

**Example 3:**

    
    
    **Input:** N = 21, K = 17, W = 10
    **Output:** 0.73278

**Note:**

  1. `0 <= K <= N <= 10000`
  2. `1 <= W <= 10000`
  3. Answers will be accepted as correct if they are within `10^-5` of the correct answer.
  4. The judging time limit has been reduced for this question.


Similar Questions:

"""


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
