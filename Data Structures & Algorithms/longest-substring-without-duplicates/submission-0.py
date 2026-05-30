class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashset = set()
        if len(s) <= 1:
            return len(s)
        l, r = 0, 0
        longest = 0
        while r < len(s) and l<len(s):
            mp = {} # char -> ind
            while r<len(s) and s[r] not in mp:
                mp[s[r]] = r
                r += 1
            longest = max(longest, r-l)
            if r == len(s):
                break
            
            l = mp[s[r]]+1
            r = l
        return longest