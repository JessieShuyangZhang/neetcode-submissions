class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs: 
            res += str(len(st)) + "#" + st
        return res # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j+1
            j = i+size
            res.append(s[i:j])
            i = j
        
        return res
