'''
link: https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        def traversal(curr, depth=0):
            if curr:
                if len(ans) == depth: ans.append(None)
                ans[depth] = curr.val
                if curr.left: traversal(curr.left, depth + 1)
                if curr.right: traversal(curr.right, depth + 1)
        traversal(root)
        return ans


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

    
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans, level = [], [root]
        while level:
            for node in level:
                if node: ans.append(node.val); break
            level = [next_node for node in level if node for next_node in (node.right, node.left)]
        return ans