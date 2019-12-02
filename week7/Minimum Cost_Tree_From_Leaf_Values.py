'''
link: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
'''

import sys
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''Dynamic Programing
        O(N ^ 2) / O(N ^ 2)
        '''
        dp = [[0] * len(arr) for _ in range(len(arr))]
        
        for i in range(len(dp)-1):
            dp[i][i+1] = arr[i] * arr[i + 1]
        for d in range(2, len(dp) + 1):
            for i in range(len(dp) - d):
                j = i + d
                for k in range(i, j):
                    if dp[i][j] == 0: 
                        dp[i][j] = max(arr[i:k+1] + [0]) * max(arr[k+1:j+1] + [0]) + dp[i][k] + dp[k+1][j]
                    else: 
                        dp[i][j] = min(dp[i][j], max(arr[i:k+1] + [0]) * max(arr[k+1:j+1] + [0]) + dp[i][k] + dp[k+1][j])
        return len(arr) and dp[0][len(arr)-1]
    
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''Stack
        O(N) / O(N)
        '''
        stack, ans = [], 0
        for i in range(len(arr)):
            
            if stack is None or len(stack) <= 1: stack.append(arr[i])
            else:
                if stack[-2] >= arr[i]:
                    pop = stack.pop(-1)
                    ans, stack =  ans + pop * arr[i], stack + [max(arr[i], pop)]
                else:
                    pop1 = stack.pop(-1)
                    pop2 = stack.pop(-1)
                    ans, stack = ans + pop1 * pop2, stack + [max(pop1, pop2), arr[i]]
        return ans + stack[-1] * stack[-2]
    
    
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''Stack
        O(N) / O(N)
        '''
        stack, ans = [float('inf')], 0
        
        for i in range(len(arr)):
            while stack[-1] <= arr[i]:
                mid = stack.pop(-1)
                ans += mid * min(arr[i], stack[-1])
            stack.append(arr[i])
        while stack and len(stack) >= 3:
            ans += stack.pop() * stack[-1]
        return ans