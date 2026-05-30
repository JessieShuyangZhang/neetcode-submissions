class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = defaultdict(set) # (i//3, j//3) --> set of digits

        for i in range(len(board)):
            for j, ch in enumerate(board[i]):
                if ch != ".":
                    if (ch in rows[i]
                        or ch in cols[j]
                        or ch in boxs[(i//3, j//3)]):
                        return False
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxs[(i//3, j//3)].add(ch)
        return True