#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        visited = set()

        def backtrack(partial_res):
            nonlocal count
            if len(partial_res) == n:
                count += 1
                return

            for i in range(1, n+1):
                if i not in visited and (i%(len(partial_res)+1) == 0 or (len(partial_res)+1)%i == 0):
                    partial_res.append(i)
                    visited.add(i)
                    backtrack(partial_res)
                    partial_res.pop()
                    visited.remove(i)
        
        backtrack([])
        return count        
# @lc code=end

