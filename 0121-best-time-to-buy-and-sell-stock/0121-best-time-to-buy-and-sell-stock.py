class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        max_profit=0
        for num in prices:
            diff= num-buy
            if diff<0:
                buy=num
            elif max_profit<diff:
                max_profit=diff
        return max_profit