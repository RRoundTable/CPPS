'''
link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_distance(self, target, candi, d):
        return d[target] - d[candi]

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        root = TreeNode(preorder[0]) 
        curr, stack, i = root, [root], 1
        while i < len(preorder):
            if curr.left is None and self.get_distance(preorder[i], curr.val, inorder_dict) < 0:
                curr.left = TreeNode(preorder[i])
                curr, stack, i = curr.left, stack + [curr.left], i + 1
            elif curr.right is None and self.get_distance(preorder[i], curr.val, inorder_dict) > 0:
                before = self.get_distance(preorder[i], curr.val, inorder_dict)
                after = self.get_distance(preorder[i], stack[-1].val, inorder_dict)
                while stack and before >= after and after > 0:
                    curr = stack.pop()
                    before = self.get_distance(preorder[i], curr.val, inorder_dict)
                    if stack: after = self.get_distance(preorder[i], stack[-1].val, inorder_dict)
                    else: break
                curr.right = TreeNode(preorder[i])
                curr, stack, i = curr.right, stack + [curr.right], i + 1
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)