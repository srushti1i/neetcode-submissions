class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top, bot=0,rows-1
        row=-1
        while top<=bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target:
                row = mid
                top = mid + 1
            else:
                bot = mid - 1
        if row==-1:
            return False
        l,r=0, cols-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid]>target:
                r=mid-1
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                return True
        return False
        
    