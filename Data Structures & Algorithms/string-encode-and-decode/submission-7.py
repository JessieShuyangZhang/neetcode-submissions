class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        5#Hello5#World
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            sublen = int(s[i:j])
            res.append(s[j+1:j+1+sublen])
            i = j+1+sublen
        return res