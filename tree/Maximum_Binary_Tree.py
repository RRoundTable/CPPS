'''
link: https://leetcode.com/problems/maximum-binary-tree/

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    O(N^2)/O(1)
    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(part):
            if not part: return None
            max_v, max_idx = -float('inf'), None
            for i, val in enumerate(part):
                if val > max_v:
                    max_v, max_idx = val, i
            node = TreeNode(max_v)
            node.left = build(part[:max_idx])
            node.right = build(part[max_idx+1:])
            return node
        return build(nums)