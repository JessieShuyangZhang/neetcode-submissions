class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r, n=0,1, len(prices)
        res = 0
        while r<n:
            if prices[l] >= prices[r]:
                l = r
                r = l+1
                continue
            else:
                prof = prices[r]-prices[l]
                if prof > res:
                    res = prof
                r += 1
           
        return res