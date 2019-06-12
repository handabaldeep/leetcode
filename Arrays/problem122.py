# Problem-122: Best Time to Buy and Sell Stock II
# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n_maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                n_maxprofit += prices[i] - prices[i-1]
        return n_maxprofit