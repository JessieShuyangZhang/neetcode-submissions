class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def bfs(source, flip: bool):
            nonlocal visited
            q = deque(source)
            while q:
                r, c = q.popleft()
                for d0, d1 in DIRS:
                    nr, nc = r + d0, c + d1
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and board[nr][nc] == "O"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        if flip:
                            board[nr][nc] = "X"

        edgeOs = []
        for i in range(ROWS):
            for j in [0, COLS - 1]:
                if board[i][j] == "O":
                    edgeOs.append((i, j))
        for j in range(COLS):
            for i in [0, ROWS - 1]:
                if board[i][j] == "O":
                    edgeOs.append((i, j))
        bfs(edgeOs, False)

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
                    bfs([(i, j)], True)
