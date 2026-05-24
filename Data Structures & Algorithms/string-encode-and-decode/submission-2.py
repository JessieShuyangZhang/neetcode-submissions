class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs: 
            res += str(len(st)) + "#" + st
        return res # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i, j = 0, 1
        while i<len(s) and j<len(s):
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j+1
            res.append(s[i:i+size])
            i += size
            j = i+1
        
        return res