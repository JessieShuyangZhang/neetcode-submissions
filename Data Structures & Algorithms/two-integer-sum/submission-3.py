class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(nums)):
            remain = target - nums[i]
            if len(mp.get(remain,[])) != 0:
                indexes = mp[remain]
                return [mp[remain][0], i]
            mp[nums[i]].append(i)
        return []