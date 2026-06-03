class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIsland = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='0':
                    continue
                q.append([i,j])
                grid[i][j] = '0'
                numIsland += 1
                while q:
                    x, y = q.popleft()
                    grid[x][y] = '0'
                    for dir in directions:
                        adj_i = x+dir[0]
                        adj_j = y+dir[1]
                        if (-1<adj_i<len(grid) 
                            and -1<adj_j<len(grid[0])
                            and grid[adj_i][adj_j] == '1'):
                            q.append([adj_i,adj_j])


        return numIsland