class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        isAtl = lambda i,j: i==ROWS-1 or j==COLS-1
        isPac = lambda i,j: i==0 or j==0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        
        def bfs(x,y):
            canAtl = isAtl(x,y)
            canPac = isPac(x,y)
            if canAtl and canPac:
                return True
            q = deque()
            visited = set()
            q.append([x,y])
            visited.add((x,y))
            while q:
                r,c = q.popleft()
                for d0,d1 in dirs:
                    nr,nc= r+d0,c+d1
                    if (-1<nr<ROWS and -1<nc<COLS 
                        and heights[nr][nc]<=heights[r][c]
                        and (nr,nc) not in visited):
                        if isAtl(nr,nc):
                            canAtl = True
                        if isPac(nr,nc):
                            canPac = True
                        if canAtl and canPac: 
                            return True
                        q.append([nr,nc])
                        visited.add((nr,nc))
            return False
        
        res=[]
        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i,j):
                    res.append([i,j])

        return res