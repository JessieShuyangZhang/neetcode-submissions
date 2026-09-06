class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] *n
        res = []
        for i in range(n):
            if i-1 >= 0:
                left[i] = left[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            if i+1 < n:
                right[i] = right[i+1]*nums[i+1]
        
        for i in range(n):
            res.append(left[i]*right[i])
        return res