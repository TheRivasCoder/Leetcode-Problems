class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            min_price = min(prices[i], min_price)
            current = prices[i] - min_price
            max_profit = max(max_profit, current)
        return max_profit