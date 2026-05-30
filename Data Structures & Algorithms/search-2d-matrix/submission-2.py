class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow , rrow = 0, len(matrix)-1
        while lrow <= rrow:
            mrow = (lrow+rrow)//2
            mrowfirst = matrix[mrow][0]
            mrowlast = matrix[mrow][-1]
            if target == mrowfirst or target == mrowlast:
                return True
            elif target > mrowfirst and target < mrowlast:
                break
            elif target < mrowfirst:
                rrow = mrow-1
            else:
                lrow = mrow+1

        if lrow > rrow:
            return False
        if target < matrix[mrow][0] or target>matrix[mrow][-1]:
            return False
        arr = matrix[mrow]
        l, r= 0,len(arr)-1
        while l<=r:
            m = (l+r)//2
            if arr[m] == target:
                return True
            elif target < arr[m]:
                r = m-1
            else:
                l = m+1
        return False
