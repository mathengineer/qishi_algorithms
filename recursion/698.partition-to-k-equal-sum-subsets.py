# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summation = sum(nums)
        n = summation/k
        if n!=int(n):
            return False
        n = int(n)
        
        visited = set()
        
        def check(start, k, cum=0):
            if k==0:
                return True
            
            if cum == n and check(0, k-1):
                return True
            
            for i in range(start, len(nums)):
                if i not in visited and cum+nums[i] <= n:
                    visited.add(i)
                    if check(i+1, k, cum+nums[i]):
                        return True
                    else:
                        visited.remove(i)
            return False
        

        return check(0, k)