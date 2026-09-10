class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        pac = [[0] * COLS for i in range(ROWS)]
        atl = [[0] * COLS for i in range(ROWS)]
        for j in range(COLS):
            pac[0][j] = 1
            atl[ROWS - 1][j] = 1
        for i in range(ROWS):
            pac[i][0] = 1
            atl[i][COLS - 1] = 1

        def bfs(r, c, grid, visited):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for d0, d1 in DIRS:
                    nr, nc = r + d0, c + d1
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and heights[nr][nc] >= heights[r][c]
                        and (nr, nc) not in visited
                    ):
                        q.append((nr,nc))
                        visited.add((nr, nc))
                        grid[nr][nc] = 1
        pacvis = set()
        atlvis = set()
        for i in range(ROWS):
            for j in range(COLS):
                if pac[i][j] == 1:
                    bfs(i,j,pac,pacvis)
                if atl[i][j] == 1:
                    bfs(i,j,atl,atlvis)
        for i in range(ROWS):
            for j in range(COLS):
                if pac[i][j] == 1 and atl[i][j] == 1:
                    res.append([i,j])
        return res