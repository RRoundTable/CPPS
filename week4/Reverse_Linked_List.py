'''
link:https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverseList1(self, head):
        """ interative
        O(2N)/O(N)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        path = []
        
        while True:
            path.append(head)
            if head.next:
                head = head.next
            else:
                break
        for i in range(len(path)-1, -1, -1):
            if i == 0:
                path[i].next = None
            else:
                path[i].next = path[i-1]
                
        return path[-1]
    
    def reverseList2(self, head):
        """iterative
        O(N)/O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def reverseList3(self, head):
        """recursive
        O(N)/O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head
        
        def reverse(curr=head, prev=None):
            if curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
                end = reverse(curr, prev)
                if end:
                    return end
            else:
                return prev
        prev = reverse(curr, prev)

                    return prev
    
    def reverseList4(self, head):
        """recursive
        O(N)/O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList4(head.next)
        head.next.next = head
        head.next = None
        return p