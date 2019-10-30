"""
link: https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
import math


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs2(self, head):
        """O(N)/O(1)
        :type head: ListNode
        :rtype: ListNode
        """

        def get(node):
            curr = node
            if curr.next:
                next_temp = curr.next
                return next_temp, curr
            else:
                return False, curr

        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        if not head:
            return head

        head_init = head
        n = get_length(head)

        head = head_init

        if n < 3:
            next_temp, curr = get(head)
            if next_temp:
                next_temp.next = curr
                curr.next = None
                return next_temp
            else:
                return curr

        if n == 3:
            next_temp, curr = get(head)
            last = next_temp.next
            next_temp.next = curr
            curr.next = last
            return next_temp

        for i in range(int(math.ceil(float(n) / 2))):
            if i == 0:
                next_temp1, curr1 = get(head)
                head_init = next_temp1
                next_temp2, curr2 = get(head.next.next)
                next_step = next_temp2.next
                next_temp1.next = curr1
                curr1.next = next_temp2
                next_temp2.next = curr2
                curr2.next = None

            elif i > 1:
                next_temp1, curr1 = get(next_step)
                if next_temp1:
                    next_step = next_temp1.next
                    curr2.next = next_temp1
                    next_temp1.next = curr1
                    curr2 = curr1
                    curr2.next = None
                else:
                    curr2.next = next_step

        return head_init

    def swapPairs1(self, head):
        """O(N)/O(N)
        :type head: ListNode
        :rtype: ListNode
        """

        def swap(node):
            curr = node
            next_temp = curr.next
            if next_temp:
                next_temp.next = curr
                curr.next = None
                return next_temp, curr
            else:
                curr.next = None
                return curr, curr

        if not head:
            return head

        head_init = None
        i = 0

        start = []
        prev = None
        while head:
            if i % 2 == 0:
                start.append(head)
            i += 1
            prev = head
            head = head.next

        if len(start) == 1:
            next_temp1, curr1 = swap(start[0])
            return next_temp1

        for i in range(len(start)):
            if i == 0:
                next_temp1, curr1 = swap(start[i])
                next_temp2, curr2 = swap(start[i + 1])
                head_init = next_temp1
                curr1.next = next_temp2

            elif i > 1:
                next_temp1, curr1 = swap(start[i])
                curr2.next = next_temp1
                curr2 = curr1

        return head_init
