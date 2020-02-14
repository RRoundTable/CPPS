'''
link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]]
        def traversal(curr, depth):
            if len(ans) == depth: ans.append([])
            if not curr: return
            ans[depth] = [curr.val] + ans[depth] if depth % 2 else ans[depth] + [curr.val]
            if curr.left:traversal(curr.left, depth + 1)
            if curr.right:traversal(curr.right, depth + 1)
        traversal(root, 0)
        return root and ans