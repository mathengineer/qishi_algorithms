# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        
        if l1.val <= l2.val:
            node = l1
            l1 = l1.next
        else:
            node = l2
            l2 = l2.next
            
        node.next = self.mergeTwoLists(l1, l2)
        return node