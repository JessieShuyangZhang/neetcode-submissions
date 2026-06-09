class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS=len(matrix),len(matrix[0])
        dp = {}
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        maxlen = 1
        def dfs(r,c): # strictly increasing path
            nonlocal maxlen
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            for d0,d1 in dirs:
                nr,nc = r+d0,c+d1
                if 0<=nr<ROWS and 0<=nc<COLS and matrix[nr][nc]>matrix[r][c]:
                    res = max(res,1+dfs(nr,nc))
            dp[(r,c)] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                maxlen = max(maxlen,dfs(i,j))
        return maxlen