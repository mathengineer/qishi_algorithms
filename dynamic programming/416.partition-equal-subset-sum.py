#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        n = summation/2
        
        if int(n) != n:
            return False
        
        n = int(n)

        solvable = [False for _ in range(n+1)]
        solvable[0] = True

        for i in range(len(nums)):
            bound = max(nums[i], n-sum(nums[i+1:]))
            for j in range(n, bound-1, -1):
                solvable[j] = solvable[j] or (solvable[j-nums[i]] if j-nums[i]>=0 else False)
        
        return solvable[n]
# @lc code=end

