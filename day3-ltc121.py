class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # should ideally set this to... float(infinity) or something to not matter. forget the syntax
        low = prices[0]
        profit = 0
        for i in prices:
            # previous highest profit and the current days profit
            profit = max(profit, i-low)
            # the newest low price
            low = min(low, i)
        return profit
