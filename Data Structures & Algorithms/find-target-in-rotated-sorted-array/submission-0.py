class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot
        pivot = -1
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m+1
        pivot = l

        # decide which side to search in. nums[0:l], nums[l:len(nums)]
        # [3,4,5], [1,2]
        def bs(a:int,b:int)->int:
            while a<=b:
                m=(a+b)//2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    a=m+1
                else:
                    b=m-1
            return -1

        if nums[0] <= target and (l>=1 and target <= nums[l-1]):
            return bs(0,l-1)
        elif target <= nums[-1] and nums[l] <= target:
            return bs(l,len(nums)-1)
        else:
            return -1
        