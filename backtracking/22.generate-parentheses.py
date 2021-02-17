#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from functools import lru_cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        partial_res = []
        res = []
        
        def backtrack(left, right):
            if left == 0 and right == 0:
                res.append(''.join(partial_res))
                return 

            if left > 0:
                partial_res.append('(')
                backtrack(left-1, right)
                partial_res.pop()
            if right > left:
                partial_res.append(')')
                backtrack(left, right-1)
                partial_res.pop()
        
        backtrack(n, n)
        return res

    # @lru_cache(maxsize=None)
    # def generateParenthesis(self, n: int) -> List[str]:
    #     if n == 1:
    #         return ['()']
    #     results = [f'({x})' for x in self.generateParenthesis(n-1)]
    #     for i in range(1, n):
    #         left = self.generateParenthesis(i)
    #         right = self.generateParenthesis(n-i)
    #         results.extend((x+y for x in left for y in right))
        # return list(set(results))

# @lc code=end

