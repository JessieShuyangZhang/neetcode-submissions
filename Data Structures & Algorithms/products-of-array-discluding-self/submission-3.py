class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  
        pref = [0] * n
        pref[0] = res[n-1] = 1 # is this necessary?
        
        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
        res[n-1] = pref[n-1]
        last_suff = 1
        for i in range(n-2, -1, -1):
            suff = last_suff*nums[i+1]
            res[i] = pref[i]*suff
            last_suff = suff
        
        return res 

"""
nums: [1,2,3,4]
expected: [24,12,8,6]
pref: [1,0,0,0]
res: [0,0,0,1] 

[1,0,0,0]
[1,1,2,6] - prefix

i = 2
suff = last_suff * nums[3] = 4
res[2] = pref[2]*4 = 8
last_suff = 4
i = 1
suff = 4 * nums[2] = 12
res[1] = pref[1] * 12 = 12
[0,0,8,1] 

"""