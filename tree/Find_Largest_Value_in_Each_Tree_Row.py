'''
link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

'''
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''O(N)/O(1)'''
    def largestValues(self, root: TreeNode) -> List[int]:
        queue, ans = deque([(root, 1)]) if root else [], []
        while queue:
            node, depth = queue.popleft()
            if len(ans) < depth:
                ans.append(node.val)
            ans[depth - 1] = max(ans[depth - 1], node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ans