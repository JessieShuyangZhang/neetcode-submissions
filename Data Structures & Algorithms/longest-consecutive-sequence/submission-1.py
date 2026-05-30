class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 0
        mp = defaultdict(int)

        for num in nums: 
            if not mp[num]:             
                length = mp[num-1]+1+mp[num+1]
                mp[num] = length
                mp[num - mp[num-1]] = length
                mp[num + mp[num+1]] = length

                if length > longest_len:
                    longest_len = length

        return longest_len