#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi) // 2
            # print(lo, hi)
            count = 0
            for n in nums:
                if lo <= n <= mid:
                    count += 1
            if count > mid-lo+1:
                hi = mid
            else:
                lo = mid+1
        return lo
        
        # for k, c in Counter(nums).items():
        #     if c > 1:
        #         return k
# @lc code=end

