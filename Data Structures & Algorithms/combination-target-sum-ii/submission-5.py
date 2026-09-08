class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cursum, comb):
            if cursum == target:
                res.append(comb.copy())
                return

            for ind in range(i, len(candidates)):
                if ind > i and candidates[ind - 1] == candidates[ind]:
                    continue
                if cursum + candidates[ind] > target:
                    break

                comb.append(candidates[ind])
                dfs(ind + 1, cursum + candidates[ind], comb)
                comb.pop()
                # dfs(ind + 1, cursum, comb) # why don't we need this? 

        dfs(0, 0, [])
        return res
