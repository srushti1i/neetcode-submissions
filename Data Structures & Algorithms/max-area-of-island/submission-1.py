class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        area=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return False
            grid[r][c]=0
            return (1+
            dfs(r+1,c) +
            dfs(r-1,c) +
            dfs(r,c+1) +
            dfs(r,c-1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    if area>max_area:
                        max_area=area
        return max_area