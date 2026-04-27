class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multisource bfs
        q = deque()
        fresh = time = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1],[1, 0],[0, 1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc  
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
                    
            time += 1

        return time if fresh == 0 else -1

        