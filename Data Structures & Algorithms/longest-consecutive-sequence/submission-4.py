class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num-1 not in s: 
                maxlen = 1 
                while num+maxlen in s:
                    maxlen += 1
                if maxlen > res:
                    res = maxlen
        return res