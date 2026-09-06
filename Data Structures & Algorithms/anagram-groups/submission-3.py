class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {} # counter tuple -> strs item
        for string in strs:
            counter = [0]*26
            for c in string:
                counter[ord(c)-ord('a')] += 1
            mpkey = tuple(counter)
            mp.setdefault(mpkey,[]).append(string)
        return list(mp.values())