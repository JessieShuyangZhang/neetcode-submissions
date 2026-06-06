class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 1
        longest = s[0]
        def findLongestPalin(l,r,s):
            nonlocal length, longest
            while l>-1 and r<len(s):
                if s[l]!=s[r]:
                    break
                if r-l+1>length:
                    length = r-l+1
                    longest = s[l:r+1]
                l-=1
                r+=1

        for i in range(len(s)):
            # odd palin
            l, r = i-1, i+1
            findLongestPalin(l,r,s)
            
            # even
            l,r=i,i+1
            findLongestPalin(l,r,s)
        
        return longest