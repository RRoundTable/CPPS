'''
link: https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        '''
        discuss
        '''
        len1, len2 = self.getLength(l1), self.getLength(l2)
        l1 = self.addLeadingZeros(len2-len1, l1)
        l2 = self.addLeadingZeros(len1-len2, l2)
        c, ans = self.combineList(l1, l2)
        if c>0:
            l3 = ListNode(c)
            l3.next = ans
            ans = l3
        return ans

    def getLength(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l

    def addLeadingZeros(self, n, node):
        for i in range(n):
            new = ListNode(0)
            new.next = node
            node = new
        return node

    def combineList(self, l1, l2):
        if (not l1 and not l2):
            return (0, None)
        c, new = self.combineList(l1.next, l2.next)
        s = l1.val+l2.val+c
        ans = ListNode(s%10)
        ans.next = new
        return (s/10, ans)
            
    def addTwoNumbers1(self, l1, l2):
        """Reverse
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        next_digit = 0
        l1_init = l1
        while l1 and l2:
            new_val = l1.val + l2.val + next_digit
            next_digit = 0
            if new_val >= 10:
                next_digit = 1
                new_val -= 10
            l1.val = new_val
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            elif l2.next and not l1.next:
                l1.next = ListNode(0)
            elif not l2.next and not l1.next and next_digit == 1:
                l1.next = ListNode(1)
                l2.next = ListNode(0)
                next_digit = 0
            elif l1.next and l2.next:
                pass
            else:
                break
            l1 = l1.next
            l2 = l2.next
        l1 = self.reverse(l1_init)
        return l1
                
    def reverse(self, node):
        prev = None
        curr = node
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def addTwoNumbers2(self, l1, l2):
        """Not use reversing
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1_str = ""
        l2_str = ""
        
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        
        twosum = int(l1_str) + int(l2_str)
        twosum = str(twosum)
        new_node = ListNode(int(twosum[0]))
        start = new_node
        for i in range(1, len(twosum)):
            new_node.next = ListNode(int(twosum[i]))
            new_node = new_node.next
        return start