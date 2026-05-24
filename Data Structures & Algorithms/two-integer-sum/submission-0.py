class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i, val in enumerate(nums):
            other = target - val
            if mp.get(other, None) != None:
                return [mp[other],i]
            else:
                mp[val] = i
        return []
