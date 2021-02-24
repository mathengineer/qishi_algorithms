#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        from math import inf
        heap = []
        heapq.heappush(heap, (0, k))
        get_dist_to = {i: inf for i in range(1, n+1) if i != k}
        get_dist_to[k] = 0
        visited = set()

        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))

        while heap:
            dist, u = heapq.heappop(heap)
            visited.add(u)
            if len(visited) == n:
                return dist

            for v, w in graph[u]:
                if v in visited:
                    continue

                new_dist = dist+w
                if new_dist < get_dist_to[v]:
                    get_dist_to[v] = new_dist
                    heapq.heappush(heap, (new_dist, v)) 
        return -1
# @lc code=end

