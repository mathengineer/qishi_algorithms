#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Binary search on the solution space
        lo = matrix[0][0]
        hi = matrix[-1][-1] + 1
        n = len(matrix)
        while lo < hi:
            mid = (lo+hi) // 2
            j = n - 1
            count = 0 
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j+1
            if count < k: lo = mid+1
            else: hi = mid
        return lo
        
        # Use heap
        # from queue import PriorityQueue
        # q = PriorityQueue()
        # n = len(matrix)
        # for col in range(n):
        #     q.put((matrix[0][col], (0, col)))
        # for _ in range(k):
        #     m, (row, col) = q.get()
        #     if row == n-1: continue
        #     q.put((matrix[row+1][col], (row+1, col)))
        # return m

        # from math import inf
        # n = len(matrix)
        # pointers = [0]*n
        # for _ in range(k):
        #     curr_min = inf
        #     for i, p in enumerate(pointers):
        #         if p < n and matrix[i][p] < curr_min:
        #             min_i = i
        #             curr_min = matrix[i][p]
        #     pointers[min_i] += 1
        # return curr_min

# @lc code=end

