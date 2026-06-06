class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        dirs=[[0,1],[1,0]] #,[0,-1],[-1,0]
        par = [i for i in range(ROWS*COLS+1)]
        size = [1] * (ROWS*COLS+1)

        def find(x):
            while par[x]!=x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px==py:
                return
            if size[px]>size[py]:
                size[px]+=size[py]
                par[py]=px
            else:
                size[py]+=size[px]
                par[px]=py
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != 'O':
                    continue
                id = r*COLS+c
                if r==0 or r==ROWS-1 or c==0 or c==COLS-1:
                    union(id,ROWS*COLS)
                for d0,d1 in dirs:
                    nr,nc= r+d0,c+d1
                    if -1<nr<ROWS and -1<nc<COLS and board[nr][nc]=='O':
                        nid = nr*COLS+nc
                        union(id,nid)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    id = r*COLS+c
                    if find(id) != ROWS*COLS:
                        board[r][c] = 'X'
