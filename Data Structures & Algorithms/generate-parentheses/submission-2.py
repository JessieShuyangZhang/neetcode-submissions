class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parStr = [] # list of chars that can make a paren string
        def dfs(openN,closeN):
            if openN == closeN == n:
                res.append(''.join(parStr))
                return
            if openN < n:
                parStr.append('(')
                dfs(openN+1, closeN)
                parStr.pop()
            if openN > closeN:
                parStr.append(')')
                dfs(openN,closeN+1)
                parStr.pop()
        dfs(0,0)
        return res
