class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        mp = dict(Counter(s1))
        mp2=dict(Counter(s2[0:len(s1)]))
        l, r = 0, len(s1)-1
        while r < len(s2):
            if mp == mp2:
                return True
            
            mp2[s2[l]] -= 1
            if mp2[s2[l]] == 0:
                del mp2[s2[l]]
            l+=1
            r += 1
            if r < len(s2):
                mp2[s2[r]] = 1 + mp2.get(s2[r],0)
            
        return False

