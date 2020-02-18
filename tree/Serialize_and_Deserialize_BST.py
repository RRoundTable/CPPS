'''
link: https://leetcode.com/problems/serialize-and-deserialize-bst/
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

'''

class Codec:
    def serialize(self, node: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if node:
            left = self.serialize(node.left) 
            right = self.serialize(node.right)
            return str(node.val) + '/' + left + '/' + right
        return ''
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        remain = data.split('/')
        def represent(r):
            if len(r) <= 1 or not r[0]: return None, r[1:]
            if (r[1] == '' and r[2] == ''): return TreeNode(int(r[0])), r[3:]
            curr = TreeNode(int(r[0]))
            left, r = represent(r[1:])
            right, r = represent(r)
            curr.left, curr.right = left, right
            return curr, r
        return represent(remain)[0]
    

class Codec:

    def serialize(self, node: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(node):
            return postorder(node.left) + postorder(node.right) + [node.val] if node else []
        return '/'.join(map(str, postorder(node)))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(ele) for ele in data.split('/') if ele]
        def build(l=float('-inf'), u=float('inf')):
            if not data or data[-1] < l or data[-1] > u:
                return None
            val = data.pop()
            node = TreeNode(val)
            right = build(val, u)
            left = build(l, val)
            node.left, node.right = left, right
            return node
        return build()