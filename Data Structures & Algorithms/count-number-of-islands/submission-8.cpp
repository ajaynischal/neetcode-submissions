class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int islands = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                //dfs
                if (grid[r][c] == '1') {
                    dfs(grid, r, c);
                    islands++;
                }
                
            }

        }

        return islands; 
    }

    void dfs(vector<vector<char>>& grid, int row, int col) {
        if (row < 0 || col < 0 || row >= grid.size() || col >= grid[0].size() || grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        dfs(grid, row + 1, col);
        dfs(grid, row - 1, col);
        dfs(grid, row, col + 1);
        dfs(grid, row, col - 1);


    }
};
