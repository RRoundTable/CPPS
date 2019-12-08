'''
link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        'O(N!)/O(N)'
        def search(node):
            if self.dist(root, node, target) == K:
                ans.append(node.val)
            if node.left:
                search(node.left)
            if node.right:
                search(node.right)
        ans = []
        search(root)
        return ans
    
    def dist(self, root, a, b):
        a_path, b_path = self.get_path(root, a), self.get_path(root, b)
        lca = self.lca(a_path, b_path)
        return len(a_path) - 1 + len(b_path) - 1 - 2 * lca
    
    def lca(self, path1, path2):
        lca = -1
        length = min(len(path1), len(path2))
        for i in range(length):
            if path1[i] == path2[i]: lca += 1
            else: break
        return lca

    def get_path(self, node, a, path=[]):
        if node.val == a.val: return path + [node]
        if node.left:
            res_left = self.get_path(node.left, a, path + [node])
            if res_left: return res_left
        if node.right:
            res_right = self.get_path(node.right, a, path + [node])
            if res_right: return res_right
        return False
    
    
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def get_dict(node, res_left=False, res_right=False, dist_left=float('inf'), dist_right=float('inf')):
            '''O(N)/O(N)'''
            if node.val == target.val: return True, 1
            if node.left:
                res_left, dist_left = get_dict(node.left)
            if node.right:
                res_right, dist_right = get_dict(node.right)
            if (node.left or node.right) and (res_left or res_right):
                d[node.val] = min(dist_left, dist_right)
                return True, d[node.val] + 1
            return False, float('inf')
        
        def search(node, dist):
            if d[node.val] != float('inf'):
                dist = d[node.val]
            else:
                d[node.val] = dist
            if dist == K: ans.append(node.val)    
            if node.left:
                search(node.left, dist + 1)
            if node.right:
                search(node.right, dist + 1)
        d, ans = defaultdict(lambda: float('inf')), []
        get_dict(root)
        d[target.val] = 0
        search(root, d[root.val])
        return ans