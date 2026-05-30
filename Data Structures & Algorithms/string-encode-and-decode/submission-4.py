class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += (str(len(st)) + "#" + st)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        subs = s
        while len(subs) > 0:
            before, _, after = subs.partition('#')
            l = int(before)
            res.append(after[0:l])
            subs = after[l:]
        return res

"""
["Hello","World"]
"5#Hello5#World"
"""