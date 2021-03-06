# coding=utf-8
import unittest

"""121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the _i_ th element is the price of a given
stock on day _i_.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

    
    
    **Input:** [7,1,5,3,6,4]
    **Output:** 5
    **Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                  Not 7-1 = 6, as selling price needs to be larger than buying price.
    

**Example 2:**

    
    
    **Input:** [7,6,4,3,1]
    **Output:** 0
    **Explanation:** In this case, no transaction is done, i.e. max profit = 0.


Similar Questions:
  Maximum Subarray (maximum-subarray)
  Best Time to Buy and Sell Stock II (best-time-to-buy-and-sell-stock-ii)
  Best Time to Buy and Sell Stock III (best-time-to-buy-and-sell-stock-iii)
  Best Time to Buy and Sell Stock IV (best-time-to-buy-and-sell-stock-iv)
  Best Time to Buy and Sell Stock with Cooldown (best-time-to-buy-and-sell-stock-with-cooldown)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit, val = 0, prices[0]
        for p in prices:
            profit = max(profit, p - val)
            if p - val < 0:
                val = p
        return profit


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maxProfit([]), 0)
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(s.maxProfit([7,6,4,3,1]), 0)


if __name__ == "__main__":
    unittest.main()
