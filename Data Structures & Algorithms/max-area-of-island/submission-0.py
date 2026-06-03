class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA, curA = 0,0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def bfs(r,c):
            area = 0
            q = deque()
            q.append([r,c])
            grid[r][c]=0
            while q: 
                x,y = q.popleft()
                area += 1
                for d0,d1 in directions:
                    nx,ny = x+d0,y+d1
                    if -1<nx<ROWS and -1<ny<COLS and grid[nx][ny]==1:
                        q.append([nx,ny])
                        grid[nx][ny]=0
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    curA = bfs(i,j)
                    maxA = max(maxA,curA)
        return maxA
