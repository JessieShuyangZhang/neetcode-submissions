class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in mp: 
                return [mp[other],i]
            mp[num] = i

        return []
