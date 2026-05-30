class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ind = -1
        while l<r:
            if nums[l]<nums[r]:
                ind = l
                break
            m = (l+r)//2
            if nums[l] <= nums[m]:
                l=m+1
            else:
                r=m
        if l==r:
            ind=l
        return nums[ind]