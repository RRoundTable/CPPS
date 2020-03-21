'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''O(N)/O(1)'''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 c = l1, 0
        while l1 or l2:
            l1.val += l2.val + c; c = 0
            if l1.val >= 10: l1.val -= 10; c = 1
            if l2.next or c: l1.next = l1.next if l1.next else ListNode(0)
            if l1.next or c: l2.next = l2.next if l2.next else ListNode(0)
            l1, l2 = l1.next, l2.next
        return head1
        