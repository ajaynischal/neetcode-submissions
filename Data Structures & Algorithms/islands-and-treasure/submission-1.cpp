class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        queue<pair<int, int>> q;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int r = curr.first;
            int c = curr.second;

            for (int i = 0; i < 4; i++) {
                int row = r + directions[i][0];
                int col = c + directions[i][1];

                if (row >= 0 && row < ROWS && col >= 0 && 
                    col < COLS && grid[row][col] == INT_MAX) {
                        grid[row][col] = grid[r][c] + 1;
                        q.push({row, col});
                }
            }

        }
    }
};
