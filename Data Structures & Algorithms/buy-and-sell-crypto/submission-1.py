class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, sell, maxprof = 0, 1, 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxprof = max(maxprof, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return maxprof

"""
[7,1,5,3,1,7]
l=0,r=1, 7>1
l=1,r=2, 1<5, maxprof=4
l=1,r=3, 1<3, maxprof=4
              maxprof=5
"""
