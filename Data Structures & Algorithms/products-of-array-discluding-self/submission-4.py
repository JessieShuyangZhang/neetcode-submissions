class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        res = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        res[-1] = pref[-1]
        suff = nums[-1]
        for i in range(n - 2, -1, -1):
            res[i] = pref[i] * suff
            suff *= nums[i]
        return res
