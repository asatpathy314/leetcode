class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        max_value = 0
        for price in prices:
            max_value = max(max_value, price - min_value)
            min_value = min(min_value, price)
        return max_value
