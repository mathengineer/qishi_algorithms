#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate_BST(node, min_node, max_node):
            if node == None: return True
            if min_node and node.val <= min_node.val: return False
            if max_node and node.val >= max_node.val: return False
            return validate_BST(node.left, min_node, node) and validate_BST(node.right, node, max_node)
        return validate_BST(root, None, None)
        
# @lc code=end

