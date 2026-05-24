class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 0
        s = set(nums)

        for num in s: 
            if num-1 not in s: 
                length = 1
                while num+length in s: 
                    length += 1
                if length > longest_len:
                    longest_len = length

        return longest_len