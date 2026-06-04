class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        pacgrid = [[False] * COLS for i in range(ROWS)]
        atlgrid = [[False] * COLS for i in range(ROWS)]
        pacSource = [[0, i] for i in range(COLS)] + [[i, 0] for i in range(1, ROWS)]
        atlSource = [[ROWS - 1, i] for i in range(COLS)] + [[i, COLS - 1] for i in range(ROWS - 1)]

        def bfs(source, grid):
            q = deque(source)
            while q:
                r, c = q.popleft()
                grid[r][c] = True
                for d0, d1 in dirs:
                    nr, nc = r + d0, c + d1
                    if (
                        -1 < nr < ROWS
                        and -1 < nc < COLS
                        and not grid[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append([nr, nc])

        bfs(pacSource, pacgrid)
        bfs(atlSource, atlgrid)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if pacgrid[i][j] and atlgrid[i][j]:
                    res.append([i, j])

        return res
