from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = -1
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                if i+1 < len(prices):
                    sell = prices[i+1]
                continue
            if prices[i] >= sell:
                sell = prices[i]
            if sell > buy and (sell - buy) > profit:
                profit = sell - buy

        return profit
