class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        l, r= 1, maxk
        mink = None
        while l<=r:
            m=(l+r)//2
            hours = 0
            for num in piles:
                hours += math.ceil(num/m)
            if hours > h:
                l = m+1
            else:
                mink = m
                r = m-1
        return mink