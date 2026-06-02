class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [-11] * len(nums)
        nset = set(nums)
        res = []
        def dfs(i,numset): 
            if i == len(nums) and min(perm) > -11:
                res.append(perm.copy())
                return
            
            for digit in numset:
                perm[i] = digit
                newset = numset - {digit}
                dfs(i+1, newset)
                perm[i] = -11
            
        dfs(0,nset)
        return res