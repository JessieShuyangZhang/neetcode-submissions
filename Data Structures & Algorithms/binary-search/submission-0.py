class Solution:
    def bs(self,l:int, r:int, nums:List[int], target:int) -> int:
        if l>r:
            return -1
        if l==r:
            return l if nums[l]==target else -1
        
        m = (l+r) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.bs(m+1,r,nums,target)
        else:
            return self.bs(l,m-1,nums,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0,len(nums)-1,nums,target)