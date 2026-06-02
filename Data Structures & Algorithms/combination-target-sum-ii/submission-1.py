class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # [1,2,2,4,5,6,9]
        res, comb = [], []
        def rec(i, total):
            if target == total:
                res.append(comb.copy())
                return
            j=i
            while j < len(candidates):
                if total+candidates[j] > target:
                    return
                comb.append(candidates[j])
                rec(j+1,total+candidates[j])
                comb.pop()
                j += 1
                while j < len(candidates) and candidates[j] == candidates[j-1]:
                    j += 1
                
            
        rec(0,0)
        return res