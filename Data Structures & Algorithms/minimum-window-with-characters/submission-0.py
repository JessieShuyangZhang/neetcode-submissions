class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tcount = dict(Counter(t))
        window, have, need = defaultdict(int),0,len(tcount)
        res, reslen = [-1,-1], float('inf')
        l,r = 0,0
        while r < len(s):
            window[s[r]] += 1
            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l, r+1]
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
            r += 1

        if reslen < float('inf'):
            return s[res[0]:res[1]]
        return ""
"""
S= ZAYXZ   T=ZXY 
window {   
Z:1, have=1
X:
Y:
}

"""