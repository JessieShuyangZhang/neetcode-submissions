class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Counter = [0]*26
        for c in s1:
            s1Counter[ord(c)-ord('a')] += 1
        counter = [0]*26
        for i in range(len(s1)):
            counter[ord(s2[i])-ord('a')] += 1
        
        for i in range(len(s2)-len(s1)):
            if counter == s1Counter: 
                return True
            
            counter[ord(s2[i+len(s1)])-ord('a')] += 1
            counter[ord(s2[i])-ord('a')] -= 1
        return (counter == s1Counter)