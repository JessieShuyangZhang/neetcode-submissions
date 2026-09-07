class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS-1
        while l<=r:
            m = (l+r)//2
            if target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][COLS-1]:
                l = m+1
            else:
                lcol, rcol = 0, COLS-1
                while lcol<=rcol:
                    mcol = (lcol+rcol)//2
                    if target == matrix[m][mcol]:
                        return True
                    elif target > matrix[m][mcol]:
                        lcol = mcol + 1
                    else:
                        rcol = mcol - 1
                return False
        return False