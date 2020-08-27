'''
link: https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node, is_leaf, path, remain):
            nonlocal ans
            if is_leaf and remain == 0:
                ans.append(path)
            if node.left:
                dfs(node.left, not bool(node.left.left) and not bool(node.left.right), path + [node.left.val], remain - node.left.val)
            if node.right:
                dfs(node.right, not bool(node.right.left) and not bool(node.right.right), path + [node.right.val], remain - node.right.val)
        if root:
            dfs(root, not bool(root.left) and not bool(root.right), [root.val], sum - root.val)
        
        return ans