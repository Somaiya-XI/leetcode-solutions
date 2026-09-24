class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0 

        while r < len(prices):
            if prices[l] < prices[r]: # I paied less so I can have profit
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP