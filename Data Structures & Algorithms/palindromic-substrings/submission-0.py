class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n
        for i in range(n):
            # odd 
            l,r=i-1,i+1
            while l>-1 and r<n:
                if s[l]==s[r]:
                    res += 1
                else:
                    break
                l-=1
                r+=1
            l,r=i,i+1
            while l>-1 and r<n:
                if s[l]==s[r]:
                    res += 1
                else:
                    break
                l-=1
                r+=1
        return res