'''
link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.leftsum = 0
        self.count = 1

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val, root=None):
        if not self.root: 
            self.root = Node(val)
            return 0
        
        if not root: root = self.root
  
        if root.val == val:
            root.count += 1
            return root.leftsum
        
        if root.val > val:
            root.leftsum += 1
            if not root.left: 
                root.left = Node(val)
                return 0
            return self.insert(val, root.left)
        
        if not root.right:
            root.right = Node(val)
            return root.leftsum + root.count
        
        return root.count + root.leftsum + self.insert(val, root.right)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:        
        tree = BinaryTree()
        return [tree.insert(nums[i]) for i in range(len(nums) - 1, -1, -1)][::-1]
    
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        ans[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
                
        ans = [0] * len(nums)
        sort(list(enumerate(nums)))
        return ans
    