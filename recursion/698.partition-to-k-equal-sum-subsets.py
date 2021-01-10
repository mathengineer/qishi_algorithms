# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k != 0:
            return False
        
        subset_sum = total//k
        
        nums.sort(reverse=True)
        visited = [False]*len(nums)
        
        def partition_sub(nums, start, subset_sum, cum, k, visited):
            if k == 0:
                return True
            
            if cum == subset_sum:
                return partition_sub(nums, 0, subset_sum, 0, k-1, visited)
            
            for i in range(start, len(nums)):
                if not visited[i] and cum+nums[i]<=subset_sum:
                    visited[i] = True
                    if partition_sub(nums, i+1, subset_sum, 
                                     cum+nums[i], k, visited):
                        return True
                    # Backtracing
                    visited[i] = False
                
            return False
        
        return partition_sub(nums, 0, subset_sum, 0, k, visited)