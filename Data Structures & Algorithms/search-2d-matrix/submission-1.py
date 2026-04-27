class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bot = ROWS - 1 #basically l and r for binary search
        #run binary search on all rows

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: #look at right most value
                top = row + 1
            elif target < matrix[row][0]: #smallest value in row
                bot = row - 1
            else:
                break
        
        #run binary search on correct individual rows
        # if not (top <= bot):
        #     return false
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False




        

        