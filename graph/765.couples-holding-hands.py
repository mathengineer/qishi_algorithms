#
# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
#

# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # Each person i belongs to (i//2)th couple
        # Build a graph that links ith couple with jth couple
        # if someone from ith couple holds hand with someone from jth couple
        from collections import defaultdict
        graph = defaultdict(list)
        for n in range(0, len(row), 2):
            i = row[n] // 2
            j = row[n+1] // 2
            # if i == j, the correct couple has already held hands
            if i != j:
                graph[i].append(j)
                graph[j].append(i)
        # each node in the graph has degree of two
        # no node points to itself
        # each connected component must be a cycle
        # it takes #node - 1 swaps to restore the couple order for the cycle
        visited = set()
        count = 0

        for i in range(len(row)//2):
            if i not in visited:
                stack = [i]
                visited.add(i)
                num_nodes = 0
                while stack:
                    node = stack.pop()
                    num_nodes += 1
                    for j in graph[node]:
                        if j not in visited:
                            stack.append(j)
                            visited.add(j)
                count += num_nodes - 1
        
        return count


# @lc code=end

