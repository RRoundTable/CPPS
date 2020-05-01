'''
link: https://leetcode.com/problems/reorder-list/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        left, right, stop = head, head, False
        
        def recurse(right):
            
            nonlocal left, stop
            if not right:
                return
    
            prev, right = right, right.next
            recurse(right)
            if left == prev or (prev and prev.next == left):
                stop = True
            if not stop:
                next_, left.next= left.next, prev
                left, prev.next = next_, next_


        recurse(right)
        left.next = None
        
            
        
            
            
                
        
                
        