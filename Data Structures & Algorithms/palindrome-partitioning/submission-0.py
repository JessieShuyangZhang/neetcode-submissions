class Solution:
    def isPalin(self,s:str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res, split = [],[]
        def getRemainingSplits(startInd):
            if startInd == len(s):
                res.append(split.copy())
                return
            for i in range(startInd,len(s)):
                if self.isPalin(s[startInd:i+1]):
                    split.append(s[startInd:i+1])
                    getRemainingSplits(i+1)
                    split.pop()
        getRemainingSplits(0)
        return res