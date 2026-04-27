class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        area = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c): 
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0 

            grid[r][c] = 0
            res = 0
            
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            
            res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        
        return area

            

        