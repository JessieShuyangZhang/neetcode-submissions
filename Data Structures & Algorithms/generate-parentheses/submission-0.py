class Solution:
    def isValidWip(self,par:list[str]) -> bool:
        stack = []
        for c in par: 
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                stack.pop()
            else:
                return False
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parCount = {'(':n, ')':n}
        parStr = [] # list of chars that can make a paren string
        def dfs():
            if len(parStr) == n*2:
                res.append(''.join(parStr))
                return
            for ch, cnt in parCount.items():
                if cnt > 0:
                    parCount[ch] -= 1
                    parStr.append(ch)
                    if self.isValidWip(parStr):
                        dfs()
                    parStr.pop()
                    parCount[ch] += 1
        dfs()
        return res
