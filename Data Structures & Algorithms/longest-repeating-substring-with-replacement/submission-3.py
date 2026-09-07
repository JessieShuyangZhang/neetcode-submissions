class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        counter = [0] * 26

        for r in range(len(s)):
            counter[ord(s[r]) - ord('A')] += 1
            while (r-l+1)-max(counter) > k:
                counter[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res