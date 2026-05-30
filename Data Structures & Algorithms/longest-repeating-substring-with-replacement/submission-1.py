class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set()
        for c in s:
            charset.add(c)
        res = 0

        for c in charset:
            l = count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                if (r-l+1) - count > k:
                    if s[l] == c:
                        count-=1
                    l += 1
                else:
                    res = max(res, (r-l+1))

        return res