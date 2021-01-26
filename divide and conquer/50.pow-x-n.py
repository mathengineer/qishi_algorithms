#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n%2 == 0:
            return self.myPow(x, n//2)*self.myPow(x, n//2)
        else:
            return self.myPow(x, n-1)*x
        
# @lc code=end

