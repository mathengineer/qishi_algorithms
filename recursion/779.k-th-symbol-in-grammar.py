# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        
        prev_k = (K+1)//2
        index = (K+1) % 2
        return abs(index-self.kthGrammar(N-1, prev_k))