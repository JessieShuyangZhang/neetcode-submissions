class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        q = deque()
        fresh = t = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            fruits_in_level = len(q)
            for i in range(fruits_in_level):  # process 1 BFS level
                x,y = q.popleft()
                for d0,d1 in dirs:
                    nx,ny = x+d0,y+d1
                    if (-1<nx<ROWS and -1<ny<COLS and grid[nx][ny] == 1):
                        grid[nx][ny]=2
                        q.append([nx,ny])
                        fresh -= 1
            t += 1
        if fresh == 0:
            return t
        else:
            return -1