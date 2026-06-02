class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtol = [['a','b','c'],['d','e','f'],
                ['g','h','i'],['j','k','l'],
                ['m','n','o'],['p','q','r','s'],
                ['t','u','v'],['w','x','y','z']]
        res,comb = [], []
        if len(digits) == 0:
            return []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(comb))
                return
            for letter in dtol[int(digits[i])-2]:
                comb.append(letter)
                dfs(i+1)
                comb.pop()
        dfs(0)
        return res