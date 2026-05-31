class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        curmax = max(nums[0:k])
        res = [curmax]
        l,r=0,k-1
        while r<len(nums)-1:
            l+=1
            r+=1
            if nums[r] > curmax:
                curmax=nums[r]
            elif nums[l-1] == curmax and nums[r] < curmax:
                curmax = max(nums[l:r+1])
            res.append(curmax)
        return res