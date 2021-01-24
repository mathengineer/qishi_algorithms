#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start
import math

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[M][K]means that, given K eggs and M moves,
        # what is the maximum number of floor that we can check
        # dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
        # which means we take 1 move to a floor,
        # if egg breaks, then we can check dp[m - 1][k - 1] floors.
        # if egg doesn't breaks, then we can check dp[m - 1][k] floors.
        
        # dp = [[0] * (K + 1) for i in range(N + 1)]
        # for m in range(1, N + 1):
        #     for k in range(1, K + 1):
        #         dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
        #     if dp[m][K] >= N: return m

        # optimize it to 1D
        # see https://www.kancloud.cn/kancloud/pack/70125
        dp = [0]*(K+1)
        for m in range(1, N+1):
            for i in range(K, 0, -1):
                dp[i] = dp[i-1]+dp[i]+1
            if dp[-1]>=N: return m


        # # https://www.youtube.com/watch?v=mLV_vOet0ss
        # # let m be the floor you drop first egg
        # solution = [[0 for _ in range(N+1)] for _ in range(K+1)]
        # solution_first_drop_at = [0 for _ in range(N+1)]
        # solution[1] = [n for n in range(N+1)]
        # for k in range(1, K+1):
        #     solution[k][1] = 1

        # n_max = N
        # for k in range(2, K):
        #     n_max = math.ceil(n_max/2)

        # for k in range(2, K+1):
        #     for n in range(2, min(n_max,N)+1):
        #         bound = min(math.ceil(n/2),n)
        #         for m in range(1, bound+1):
        #             solution_first_drop_at[m] = max(solution[k-1][m-1], solution[k][n-m])+1
        #             solution[k][n] = min(solution_first_drop_at[1:m+1])
        #     n_max *= 2
        # return solution[K][N]
        
# @lc code=end

