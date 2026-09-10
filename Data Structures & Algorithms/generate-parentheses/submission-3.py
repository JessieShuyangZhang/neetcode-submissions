class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recur(opencnt, closecnt, partial):
            if len(partial) == 2*n:
                res.append(partial)
                return
            if opencnt == n: 
                partiallen = len(partial)
                for i in range(2*n-partiallen):
                    partial += ')'
                res.append(partial)
                return
            # choice 1: add an open if the opencnt is not yet n
            recur(opencnt+1, closecnt, partial + '(')
            # choice 2: add a closed if there are more opened than closed
            if opencnt > 0 and opencnt>closecnt:
                recur(opencnt,closecnt+1, partial+')')

        recur(0,0,'')
        return res