class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r,c,visited,prevh):
            if not (-1<r<ROWS and -1<c<COLS 
                and (r,c) not in visited and heights[r][c]>=prevh):
                return

            h = heights[r][c]
            visited.add((r,c))
            dfs(r+1,c,visited,h)
            dfs(r-1,c,visited,h)
            dfs(r,c+1,visited,h)
            dfs(r,c-1,visited,h)

        for i in range(ROWS):
            dfs(i,0,pac,-1)
            dfs(i,COLS-1,atl,-1)

        for j in range(COLS):
            if j>0:
                dfs(0,j,pac,-1)
            if j<COLS-1:
                dfs(ROWS-1,j,atl,-1)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i, j])
        return res
