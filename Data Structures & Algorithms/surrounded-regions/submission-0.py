class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if r<0 or c<0 or r>ROWS-1 or c>COLS-1 or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for d0,d1 in dirs:
                dfs(r+d0,c+d1)

        for r in range(ROWS):
            for c in (0,COLS-1):
                if board[r][c] == 'O':
                    dfs(r,c)
        
        for c in range(COLS):
            for r in (0,ROWS-1):
                if board[r][c] == 'O':
                    dfs(r,c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'