class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxP = max(maxP , price - minPrice)
        return maxP
        