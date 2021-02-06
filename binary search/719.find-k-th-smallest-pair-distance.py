#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        def no_less_than_k_dist_greater_than(guess):
            count = j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j]-nums[i] <= guess: 
                    j+=1
                count += j-i-1
            return count >= k
        
        
        while lo < hi:
            mid = (lo+hi) // 2
            if no_less_than_k_dist_greater_than(mid): hi = mid
            else: lo = mid+1
        return lo
# @lc code=end

