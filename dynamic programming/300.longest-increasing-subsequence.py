# @before-stub-for-debug-begin
from python3problem300 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        max_lens = [1 for _ in nums] # max lens ending at i

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    max_lens[j] = max(max_lens[j], max_lens[i]+1)
        return max(max_lens)



        
# @lc code=end

