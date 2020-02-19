'''
link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def dp(node):
            nonlocal ans
            if node:
                left = dp(node.left)
                right = dp(node.right)
                curr_sum = max(left, 0) + max(right, 0) + node.val
                ans = max(ans, curr_sum)
                return max(left, right, 0) + node.val 
            return float('-inf')
        dp(root)
        return ans 