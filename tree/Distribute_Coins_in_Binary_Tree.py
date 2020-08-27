'''
link: https://leetcode.com/problems/distribute-coins-in-binary-tree/

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4
 

Note:

1<= N <= 100
0 <= node.val <= N

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return 0, 0
            left_need, left_have = dfs(node.left)
            right_need, right_have = dfs(node.right)
            need = left_need + right_need + 1
            have = left_have + right_have + node.val
            if not node.left and not node.right:
                need = 1
                have = node.val
            ans += abs(need - have)
            return need, have
        dfs(root)
        return ans