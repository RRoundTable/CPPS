'''
link: https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''O(KN)/O(1)'''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node = res = ListNode(-1)
        while lists and res:
            minval, minidx = float('inf'), -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minval:
                    minval, minidx = lists[i].val, i
            res.next = lists[minidx] if minidx >= 0 else None
            lists[minidx] = lists[minidx].next if lists[minidx] else None
            res = res.next
        return node.next