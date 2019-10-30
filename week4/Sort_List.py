"""
link:https://leetcode.com/problems/sort-list/
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList2(self, head):
        """O(NlogN)/O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        unsorted = []

        while head:
            unsorted.append(head)
            head = head.next

        unsorted = sorted(unsorted, key=lambda x: x.val)
        for i in range(len(unsorted) - 1):
            unsorted[i].next = unsorted[i + 1]

        unsorted[-1].next = None
        return unsorted[0]

    def sortList(self, head):
        """Merge sort: Bottom-up
        :type head: ListNode
        :rtype: ListNode
        """

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def move(node, move):
            for _ in range(move):
                node = node.next
            return node

        def merge(head1, head2, pre):
            while head1 and head2:
                if head1.val < head2.val:
                    pre.next = head1
                    head1 = head1.next
                else:
                    pre.next = head2
                    head2 = head2.next
                pre = pre.next
            pre.next = head1 if head1 is not None else head2
            return pre

        n = get_length(head)

        if n < 2:
            return head
        merge_size = 1

        dummy = ListNode(-1)
        dummy.next = head
        node = head

        while merge_size < n:
            pre = dummy
            end = None
            i = 0
            while n - i > merge_size:
                list0 = pre.next
                node = pre

                # move: left
                node = move(node, merge_size)
                i += merge_size
                # mid point

                mid = node
                # move: right
                node = move(node, min(merge_size, n - i))
                i += min(merge_size, n - i)

                end = None

                if node is not None:
                    end = node.next
                    node.next = None

                list1 = mid.next
                mid.next = None
                pre.next = None

                # merge
                pre = merge(list0, list1, pre)

                while pre.next is not None:
                    pre = pre.next
                pre.next = end
            merge_size <<= 1

        return dummy.next
