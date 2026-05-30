class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        for i in range(len(s)):
            count, maxf={},0
            for j in range(i,len(s)):
                count[s[j]]=1+ count.get(s[j],0)
                maxf = max(maxf, count[s[j]])
                if (j-i+1)-maxf <= k:
                    res = max(res,j-i+1)

        return res

"""
ABABABABABACCKSGH , k=2
count:{
A: 2
B: 2
}
i=0, j=1, maxf=1
     j=2, maxf=2
     j=3, maxf=2, 
"""