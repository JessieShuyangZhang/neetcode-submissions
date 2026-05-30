class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        res = []
        for i, st in enumerate(strs):
            sortedst = ''.join(sorted(st))
            mp[sortedst].append(st)

        for key,anas in mp.items():
            res.append(anas)
        return res