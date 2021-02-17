#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        visited = set()

        def backtrack(partial_res):
            if len(partial_res) == len(nums):
                res.append(list(partial_res))
                return

            for n in nums:
                if n not in visited:
                    partial_res.append(n)
                    visited.add(n)
                    backtrack(partial_res)
                    partial_res.pop()
                    visited.remove(n)
        
        backtrack([])
        return res
# @lc code=end

