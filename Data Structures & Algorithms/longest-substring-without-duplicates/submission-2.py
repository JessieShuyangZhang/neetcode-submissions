class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        res = 1
        mp = defaultdict(int) # char -> index
        mp[s[l]] = l
        while r<len(s) and l<=r:
            if s[r] in mp:
                l = max(l, mp[s[r]]+1)
                
            mp[s[r]] = r
            res = max(res,r-l+1)
            r += 1
        return res
