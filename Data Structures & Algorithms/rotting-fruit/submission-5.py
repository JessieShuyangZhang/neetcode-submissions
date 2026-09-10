class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        visited = set()
        numFresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    numFresh += 1
        if len(q) == 0:
            if numFresh == 0:
                return 0
            else:
                return -1

        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for d0, d1 in DIRS:
                    nr, nc = r + d0, c + d1
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            time += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return time-1