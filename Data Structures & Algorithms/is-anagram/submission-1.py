class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fm = defaultdict(int)
        for cs in s: 
            fm[cs] += 1
        for ct in t:
            fm[ct] -= 1
            if fm[ct] < 0:
                return False

        for val in fm.values():
            if val != 0:
                return False

        return True