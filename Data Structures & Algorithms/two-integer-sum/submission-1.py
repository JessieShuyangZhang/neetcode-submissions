class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, val in enumerate(nums):
            other = target - val
            if other in mp:
                return [mp[other],i]
            else:
                mp[val] = i
        return []
