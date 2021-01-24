#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = [nums[0],] # max prod end at n-1
        min_prod = [nums[0],]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                if max_prod[i-1] > 0:
                    max_prod.append(max_prod[i-1]*nums[i])
                else:
                    max_prod.append(nums[i])
                if min_prod[i-1] <= 0:
                    min_prod.append(min_prod[i-1]*nums[i])
                else:
                    min_prod.append(nums[i])
            elif nums[i] < 0:
                if min_prod[i-1] <= 0:
                    max_prod.append(min_prod[i-1]*nums[i])
                else:
                    max_prod.append(nums[i])
                if max_prod[i-1] > 0:
                    min_prod.append(max_prod[i-1]*nums[i])
                else:
                    min_prod.append(nums[i])
            else:
                max_prod.append(0)
                min_prod.append(0)
        print(max_prod)
        print(min_prod)
        return max(max_prod)


        
# @lc code=end

