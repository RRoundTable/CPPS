'''
link: https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

'''
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def traversal(curr, ans=0):
            if curr.left: ans = traversal(curr.left, ans)    
            if curr.val >= L and curr.val <= R: ans += curr.val
            if curr.val > R: return ans
            if curr.right: ans = traversal(curr.right, ans)
            return ans
        return traversal(root)


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, ans,visited = [], 0, set()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.val >= L and node.val <= R: ans += node.val
            if node.val not in visited:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return ans