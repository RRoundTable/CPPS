"""
link:https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def reverseList(head, k):
            """iterative
            O(N)/O(1)
            :type head: ListNode
            :rtype: ListNode
            """
            prev = None
            curr = head
            curr_init = head
            for _ in range(k):

                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev, curr_init, next_temp

        n = get_length(head)

        if n < 2:
            return head

        ngroup = n // k

        if ngroup == 0:
            return head

        leftout = n % k
        prev = None
        while ngroup > 0:
            if prev is None:
                start, prev, head = reverseList(head, k)
            else:
                start_, prev_, head_ = reverseList(head, k)
                prev.next = start_
                prev = prev_
                head = head_
            ngroup -= 1
            if ngroup == 0 and leftout > 0:
                prev.next = head
        return start

