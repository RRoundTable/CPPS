'''
link:https://leetcode.com/problems/subtree-of-another-tree/
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''O(N^2)/O(N^2)'''
        def dfs(node, result=False):
            if node.val == t.val:
                result = self.check(node, t)
                if result: return result
            if node.left is not None:
                result = dfs(node.left)
                if result: return True
            if node.right is not None:
                result = dfs(node.right)
                if result: return True
            return result
        return dfs(s)
    
    def check(self, a, b):
        if a.val != b.val: return False
        if (a.left and not b.left) or (not a.left and b.left):
            return False
        if (a.right and not b.right) or (not a.right and b.right):
            return False
        if a.left and b.left:
            result = self.check(a.left, b.left)
            if not result: return False
        if a.right and b.right:
            result = self.check(a.right, b.right)
            if not result: return False
        return True
