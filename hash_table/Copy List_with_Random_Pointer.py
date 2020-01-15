'''
link: https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''O(N)/O(N)
        Iterative
        '''
        d, ans, start = {None: [None, None, None]}, None, head
        while head != None:
            d[head] = [head.next, head.random, Node(head.val)]
            if ans is None: ans = d[head][2];
            head = head.next
        head = start
        while head != None:
            next_node, rand_node, copy = d[head]
            copy.next, copy.random = d[next_node][2], d[rand_node][2]
            head = head.next
        return ans 
    

    
class Solution:
    def __init__(self):
        self.d = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''O(N)/O(N)
        Recursive
        '''
        if head is None: return None
        if self.d.get(head, None) is None:
            self.d[head] = Node(head.val)
        else:
            return self.d[head]
        if self.d[head].next is None and head.next is not None:
            self.d[head].next = self.copyRandomList(head.next)
        if self.d[head].random is None and head.random is not None:
            self.d[head].random = self.copyRandomList(head.random)
        return self.d[head]
        
    
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''O(N)/O(1)
        Iterative with O(1) space
        '''
        if head is None: return None
        ans, start, copy = None, head, None
        while head != None:
            copy = Node(head.val, head.next)
            if ans is None: ans = copy;
            copy.next, head.next = head.next, copy
            head = copy.next
            
        head = start
        while head != None:
            head.next.random = head.random.next if head.random else None
            head = head.next.next
            
        head = start
        while head != None:
            next_head = head.next.next
            head.next.next = head.next.next.next if head.next.next else None
            head = next_head
        return ans