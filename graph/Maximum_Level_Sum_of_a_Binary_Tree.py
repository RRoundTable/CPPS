'''
link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    '''O(N)/O(N)'''
    def maxLevelSum(self, root: TreeNode) -> int:
        ans, pre, queue = [0, 0], [1, 0], deque([[root, 1]])
        while queue:
            node, level = queue.popleft()
            if level > pre[0]:
                if ans[1] < pre[1]: ans = pre
                pre = [level, 0]
            pre[1] += node.val
            if node.left: queue.append([node.left, level + 1])
            if node.right: queue.append([node.right, level + 1])
        return ans[0]