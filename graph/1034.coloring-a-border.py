#
# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#

# @lc code=start
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        component_color = grid[r0][c0]
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0 # mark visited
            for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if r == -1 or r == m or c == -1 or c == n:
                    grid[i][j] = -1 # adj to grid border, mark board
                elif grid[r][c] == component_color:
                    dfs(r, c)
                elif 1<= grid[r][c] <= 1000:
                    grid[i][j] = -1 # adj to other color, mark board

        dfs(r0, c0)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = component_color
                elif grid[i][j] == -1:
                    grid[i][j] = color
        
        return grid

# @lc code=end

