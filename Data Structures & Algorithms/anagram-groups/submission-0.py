class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {} # first sorted occur -> list of indexes
        for i, val in enumerate(strs):
            val_sorted = "".join(sorted(val))
            if val_sorted in mp: 
                mp[val_sorted].append(i)
            else:
                mp[val_sorted] = [i]
        arr = []
        for _,vals in mp.items():
            anagrams = []
            for ind in vals:
                anagrams.append(strs[ind])
            arr.append(anagrams)
        return arr

    # def isAnagram(s, t) -> bool:
    #     if len(s) ! len(t):
    #         return False
    #     arr = [0]*26
    #     for i in range(len(s)):
    #         arr[ord(s[i]) - ord('a')] += 1
    #         arr[ord(t[i]) - ord('a')] -= 1
    #     for el in arr:
    #         if el != 0:
    #             return False
    #     return True
