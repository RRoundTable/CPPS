'''
link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def dfs(node):
            nonlocal s
            if node:
                s += node.val
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        def inorder(node):
            nonlocal s
            if node:
                inorder(node.left)
                curr = node.val; node.val = s; s -= curr
                inorder(node.right)
        inorder(root)
        return root
        
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''Reversed Inorder traversal'''
        s = 0
        def rinorder(node):
            nonlocal s
            if node:
                rinorder(node.right)
                curr = node.val; s += curr; node.val = s;
                rinorder(node.left)
        rinorder(root)
        return root