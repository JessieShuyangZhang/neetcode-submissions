class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        sizes = []
        for st in strs: 
            sizes.append(len(st))

        res = ",".join(str(size) for size in sizes) + "#"
        for st in strs:
            res += st
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        encoded_sizes, sep, encoded_strs = s.partition("#")
        sizes = encoded_sizes.split(",")
        res = []
        currsize = 0
        for size_str in sizes: 
            size = int(size_str)
            st = encoded_strs[currsize : currsize+size]
            res.append(st)
            currsize += size
        return res