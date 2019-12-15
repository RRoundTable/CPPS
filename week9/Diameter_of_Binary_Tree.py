'''
link: https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''O(N^2)/O(1)'''
        def search(node, depth):
            if node is None: return depth
            d1 = search(node.left, depth + 1)
            d2 = search(node.right, depth + 1)
            return max(d1, d2) 
        self.ans = 0
        def dfs(node):
            if node is None: return
            left, right = search(node.left, 0), search(node.right, 0)
            self.ans = max(self.ans, left + right)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
    
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''O(N)/O(N)'''
        self.d, self.ans = {}, 0
        def search(node):
            if node is None: return 0
            if self.d.get(node, False): return self.d[node]
            d1 = search(node.left)
            d2 = search(node.right)
            self.d[node] = max(d1, d2) + 1
            return self.d[node]
        
        def dfs(node):
            if node is None: return
            left, right = search(node.left), search(node.right)
            self.ans = max(self.ans, left + right)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
        
        