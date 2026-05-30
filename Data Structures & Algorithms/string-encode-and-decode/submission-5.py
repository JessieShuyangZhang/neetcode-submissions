class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += (str(len(st)) + "#" + st)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while j < len(s):
            if s[j] == '#':
                l = int(s[i:j])
                i = j+1
                j=i+l
                res.append(s[i:j])
                i = j
            else:
                j += 1

        return res

"""
["Hello","World"]
"5#Hello5#World"
"""