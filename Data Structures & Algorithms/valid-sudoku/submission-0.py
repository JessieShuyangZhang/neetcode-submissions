class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mp_row = {k: defaultdict(int) for k in range(9)}
        mp_col = {k: defaultdict(int) for k in range(9)}
        mp_box = defaultdict(lambda: defaultdict(int))
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit == ".": 
                    continue;
                
                if mp_row[i][digit] > 0:
                    return False
                if mp_col[j][digit] > 0:
                    return False
                box_ind = (i // 3, j // 3)
                if mp_box[box_ind][digit] > 0:
                    return False
                mp_row[i][digit] += 1
                mp_col[j][digit] += 1
                mp_box[box_ind][digit] += 1
        return True
