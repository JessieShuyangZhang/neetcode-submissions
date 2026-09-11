class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, houses: List[int]) -> int:
        n = len(houses)
        if n == 1:
            return houses[0]
        cache = [0] * (n)
        cache[0] = houses[0]
        cache[1] = max(houses[0], houses[1])
        for i in range(2, n):
            cache[i] = max(cache[i-1], cache[i-2]+houses[i])
        return cache[-1]