# coding=utf-8
import unittest

"""933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/description/

Write a class `RecentCounter` to count recent requests.

It has only one method: `ping(int t)`, where t represents some time in
milliseconds.

Return the number of `ping`s that have been made from 3000 milliseconds ago
until now.

Any ping with time in `[t - 3000, t]` will count, including the current ping.

It is guaranteed that every call to `ping` uses a strictly larger value of `t`
than before.  



**Example 1:**

    
    
    **Input:** inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
    **Output:** [null,1,2,3,3]



**Note:**

  1. Each test case will have at most `10000` calls to `ping`.
  2. Each test case will call `ping` with strictly increasing values of `t`.
  3. Each call to ping will have `1 <= t <= 10^9`.


Similar Questions:

"""

from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.t = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.t.append(t)
        while t - self.t[0] > 3000:
            self.t.popleft()
        return len(self.t)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class T(unittest.TestCase):
    def test(self):
        s = RecentCounter()
        self.assertEqual(s.ping(1), 1)
        self.assertEqual(s.ping(100), 2)
        self.assertEqual(s.ping(3001), 3)
        self.assertEqual(s.ping(3002), 3)


if __name__ == "__main__":
    unittest.main()
