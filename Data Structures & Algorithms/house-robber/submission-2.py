class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0] * (n+1)
        money[n] = 0
        money[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            money[i] = max(money[i+1], money[i+2]+nums[i])
        return max(money[0], money[1])