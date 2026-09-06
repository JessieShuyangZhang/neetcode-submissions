class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        boxmap = defaultdict(set)  # box: (i//3, j//3)

        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != '.':
                    num = board[i][j]
                    if (num in rowmap[i]) or (num in colmap[j]) or (num in boxmap[(i//3,j//3)]):
                        return False
                    rowmap[i].add(num)
                    colmap[j].add(num)
                    boxmap[(i//3,j//3)].add(num)
        return True