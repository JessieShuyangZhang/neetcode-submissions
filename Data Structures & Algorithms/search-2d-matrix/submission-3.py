class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        while col>-1 and row<len(matrix):
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -=1
            else:
                return True
        return False