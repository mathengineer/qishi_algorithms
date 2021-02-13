#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        class UnionFind:
            def __init__(self, n):
                self.parents = list(range(n))
                self.sizes = [1]*n
                self.roots = set(range(n))
            
            def find(self, x):
                while self.parents[x] != x:
                    # compress path
                    self.parents[x] = self.parents[self.parents[x]]
                    x = self.parents[x]
                return x
            
            def is_connected(self, x, y):
                return self.find(x) == self.find(y)
            
            def union(self, x, y):
                if self.is_connected(x, y):
                    return
                
                x_root = self.find(x)
                y_root = self.find(y)
                if self.sizes[x_root] >= self.sizes[y_root]:
                    self.parents[y_root] = x_root
                    self.sizes[x_root] += self.sizes[y_root]
                    self.roots.remove(y_root)
                else:
                    self.parents[x_root] = y_root
                    self.sizes[y_root] += self.sizes[x_root]
                    self.roots.remove(x_root)
        
        uf = UnionFind(len(grid)*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                            uf.union(i*len(grid[0])+j, x*len(grid[0])+y)
        count = 0
        for n in uf.roots:
            i, j = n//len(grid[0]), n%len(grid[0])
            if grid[i][j] == '1':
                count += 1
        return count


        # # DFS
        # if not grid: return 0
        # stack = []
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             count += 1
        #             stack.append((i, j))
        #             while stack:
        #                 m, n = stack.pop()
        #                 grid[m][n] = 'x' # mark as visited
        #                 for x, y in ((m-1, n), (m+1, n), (m, n-1), (m, n+1)):
        #                     if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
        #                         stack.append((x, y))
        
        # return count
# @lc code=end

