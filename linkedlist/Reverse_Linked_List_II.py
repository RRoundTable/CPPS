'''
link: https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


class Solution:
    '''Iterative'''
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i, head = 0, ListNode(-1, head)
        dummy = prev = head
        while head:
            if i == m: m_node, m_prev = head, prev
            if i == n: n_node, n_next = head, head.next
            if i >= m + 1 and i <= n:
                head_next, head.next, prev = head.next, prev, head
                head, i = head_next, i + 1
            else:
                head, prev, i = head.next, head, i + 1
            if i - 1 == n:
                m_prev.next, m_node.next = n_node, n_next
        return dummy.next
    
    
class Solution:
    '''Recursion'''
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        head, left, right, stop = ListNode(-1, head), head, head, False
        
        def recurse(right, m, n):
            nonlocal left, stop
            if n == 1: return
            right = right.next
            if m > 1: left = left.next
            recurse(right, m - 1, n - 1)
            if left == right or right.next == left: stop = True
            if not stop:
                left.val, right.val, left = right.val, left.val, left.next                
        recurse(right, m, n)
        return head.next