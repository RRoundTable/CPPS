'''
link: https://leetcode.com/problems/recover-binary-search-tree/
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
class Solution:
    def recoverTree(self, node: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''O(N^2)/O(N)'''
        def search(node):
            preorder.append(node.val)
            if node.left:
                search(node.left)
            inorder.append(node.val)
            if node.right:
                search(node.right)
        
        def dfs(node, preorder):
            node.val = preorder.pop()
            if node.left:
                dfs(node.left, preorder)
            if node.right:
                dfs(node.right, preorder)
                
        def find(inorder):
            base = sorted(inorder)
            for i in range(len(inorder)):
                for j in range(i + 1, len(inorder)):
                    if inorder != base:
                        inorder[i], inorder[j] = inorder[j], inorder[i]
                        if inorder == base:
                            return i, j
                        inorder[i], inorder[j] = inorder[j], inorder[i]
            
        preorder, inorder = [], []
        predict, indict = {}, {}
        search(node)
        base = sorted(inorder)
        for i in range(len(preorder)):
            predict[preorder[i]] = i
        i, j = find(inorder)
        i, j = predict[inorder[i]], predict[inorder[j]]
        preorder[i], preorder[j] = preorder[j], preorder[i]
        preorder.reverse()
        dfs(node, preorder)
        
class Solution:
    def recoverTree(self, node: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def search(node):
            if node.left:
                search(node.left)
            inorder.append(node)
            if node.right:
                search(node.right)
        inorder, wrong = [], []
        search(node)
        for i, node in enumerate(inorder):
            if node.left is None:
                if i != 0 and node.val < inorder[i-1].val:
                    wrong += [inorder[i-1], node]
            if node.right is None:
                if i != len(inorder) - 1 and node.val > inorder[i+1].val:
                    wrong += [node, inorder[i+1]]
        right = sorted(wrong, key=lambda x: x.val)
        right = [r.val for r in right]
        for w, r in zip(wrong, right):
            w.val = r
            
        
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops = root, TreeNode(float('-inf')), []
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur: temp = temp.right
                if not temp.right:
                    temp.right, cur = cur, cur.left
                    continue
                temp.right = None
            if cur.val < prev.val: drops.append((prev, cur))
            prev, cur = cur, cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

        
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """O(N) / O(H)
        Do not return anything, modify root in-place instead.
        """
        def traverse(node: TreeNode) -> None:
            if not node: return
            traverse(node.left)
            if self.recent and node.val < self.recent.val:
                if not self.fix: self.fix = [self.recent, node]
                else: self.fix[1] = node
            self.recent = node
            traverse(node.right)
        self.recent = self.fix = None; traverse(root)
        self.fix[0].val, self.fix[1].val = self.fix[1].val, self.fix[0].val


        
        
        
        
