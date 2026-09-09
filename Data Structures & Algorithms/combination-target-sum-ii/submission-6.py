class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def recur(ind, cursum, comb):
            if cursum == target:
                res.append(comb.copy())
                return
            if ind >= len(candidates) or cursum > target:
                return
            
            comb.append(candidates[ind])
            recur(ind+1, cursum+candidates[ind], comb)
            comb.pop()

            while ind+1<len(candidates) and candidates[ind] == candidates[ind+1]:
                ind += 1
            recur(ind+1, cursum, comb)
        recur(0, 0, [])
        return res