'''
link: https://leetcode.com/problems/count-complete-tree-nodes/
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
from collections import Counter

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, node: TreeNode) -> int:
        '''O(N)/O(N)'''
        depth = self.depth(node)
        Count = Counter(depth)
        if depth is None: return 0
        return 2 ** max(depth) - 1 - (2 ** (max(depth) - 1) - Count[max(depth)])
    
    def depth(self, node: TreeNode, count=1, depth=[]) -> int:
        if node is None: return None
        if node.left is None and node.right is None:
            return depth + [count]
        if node.left is not None:
            depth = self.depth(node.left, count + 1, depth)
        if node.right is not None:
            depth = self.depth(node.right, count + 1, depth)
        return depth
