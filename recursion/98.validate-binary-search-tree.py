# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def valid_bst_max_min(node):
            # return whether the tree is BST, max and min in the tree
            if node == None:
                return True, None, None
            
            # if the subtree is not bst, max and min do not matter
            left_valid_bst, left_max, left_min = valid_bst_max_min(node.left)
            if not left_valid_bst:
                return False, None, None
            
            right_valid_bst, right_max, right_min = valid_bst_max_min(node.right)
            if not right_valid_bst:
                return False, None, None
            
            if (left_max and left_max >= node.val) or (right_min and right_min <= node.val):
                return False, None, None
            
            if left_min is None:
                curr_min = node.val
            else:
                curr_min = left_min
                
            if right_max is None:
                curr_max = node.val
            else:
                curr_max = right_max
                
            return True, curr_max, curr_min
        
        valid_bst, _, _ = valid_bst_max_min(root)
        return valid_bst