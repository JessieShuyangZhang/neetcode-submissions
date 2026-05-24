class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff, res = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        
        pref[0], suff[-1] = 1,1
        for i in range(1, len(nums)):
            pref[i] = pref[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i] = pref[i]*suff[i]
        return res 

