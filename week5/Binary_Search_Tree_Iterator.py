"""
link: https://leetcode.com/problems/binary-search-tree-iterator/

mplement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """avg(1)/O(h)
        :type root: TreeNode
        """
        self.root = root
        self.stack = self.get_stack(root)
        self.current = None

    def get_stack(self, root):
        cur = root
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.left
        return stack

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.current = self.stack.pop(-1)
        value = self.current.val
        if self.current.right is not None:
            self.current = self.current.right
            add_stack = self.get_stack(self.current)
            self.stack += add_stack
        elif self.stack:
            pass
        return value

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.current and not self.stack:
            return False

        if self.stack or self.current.right:
            return True
        else:
            return False
