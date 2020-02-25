'''
link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def post(node):
            nonlocal ans
            if node:
                post(node.left)
                post(node.right)
                ans.append(node.val)
        post(root)
        return ans
    
    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack, visited = [], [root], set()
        while root and stack:
            node = stack[-1]
            if not node.left and not node.right or node in visited:
                ans.append(stack.pop().val); continue
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            visited.add(node)
        return ans