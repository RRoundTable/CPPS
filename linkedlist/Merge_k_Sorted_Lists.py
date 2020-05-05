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
from heapq import heappop, heappush


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


class Solution:
    '''O(NlogK)/O(1)'''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        que, res, k = [], ListNode(-1), len(lists)
        node = res
        
        for i in range(len(lists)):
            if not lists[i]: continue
            heappush(que, (lists[i].val, id(lists[i]), lists[i]))
            lists[i] = lists[i].next
        while que:
            next_ = heappop(que)[2]
            res.next = next_
            if next_.next: heappush(que, (next_.next.val, id(next_.next), next_.next))
            res = res.next
            
        return node.next
    
    
class Solution:
    '''O(KN)/O(1)'''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if lists else None
    
    def merge(self, l1, l2):
        head = point = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:point.next, l1 = l1, l1.next
            else: point.next, l2 = l2, l2.next
            point = point.next
        if l1: point.next = l1
        else: point.next = l2
        return head.next