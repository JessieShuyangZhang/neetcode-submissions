class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        maxl = 0
        for num in nums:
            if mp[num] != 0:
                continue

            length = mp[num - 1] + 1 + mp[num + 1]
            mp[num] = length
            mp[num - mp[num - 1]] = length
            mp[num + mp[num + 1]] = length
            if length > maxl:
                maxl = length
        return maxl