class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # STEP 1: find correct row
        top, bottom = 0, rows - 1
        row = -1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target:
                row = mid
                top = mid + 1
            else:
                bottom = mid - 1

        if row == -1:
            return False

        # STEP 2: binary search in that row
        l, r = 0, cols - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False