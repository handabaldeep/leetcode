# Problem-121: Best Time to Buy and Sell Stock
# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        n_min = prices[0]
        n_maxprice = 0
        for i in range(1,len(prices)):
            if prices[i]<n_min:
                n_min = prices[i]
            elif prices[i]-n_min > n_maxprice:
                n_maxprice = prices[i]-n_min
        return n_maxprice