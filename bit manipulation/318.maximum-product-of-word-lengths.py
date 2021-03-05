#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = [(set(w), len(w)) for w in words]
        res = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not words[i][0] & words[j][0] and words[i][1]*words[j][1] > res:
                    res = words[i][1]*words[j][1]
                    
        return res
        
# @lc code=end

