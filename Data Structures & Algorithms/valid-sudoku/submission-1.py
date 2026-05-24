class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit == ".": 
                    continue;
                box_ind = (i//3,j//3)
                if (digit in rows[i]
                    or digit in cols[j]
                    or digit in boxes[box_ind]):
                    return False
                
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[box_ind].add(digit)
        return True
