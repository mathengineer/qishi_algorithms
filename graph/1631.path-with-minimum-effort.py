#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # similar to Dijkstra
        import heapq
        from math import inf
        m = len(heights)
        n = len(heights[0])
        cost_to_get = {(i, j): inf 
                        for i in range(m)
                        for j in range(n)}
        heap = []
        heapq.heappush(heap, (0, (0, 0)))
        visited = set()

        while heap:
            effort, (i, j) = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return effort

            visited.add((i, j))

            for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (r, c) in visited:
                    continue

                if 0<=r<m and 0<=c<n:
                    new_effort = max(effort, abs(heights[i][j]-heights[r][c]))
                    if cost_to_get[(r, c)] > new_effort:
                        cost_to_get[(r, c)] = new_effort
                        heapq.heappush(heap, (new_effort, (r, c)))
                
# @lc code=end

