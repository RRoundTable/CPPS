'''
link: https://leetcode.com/problems/unique-binary-search-trees/
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''


import math
class Solution:
    def numTrees(self, n: int) -> int:
        '''O(N^2)/O(N)'''
        dp = [1] * n
        for i in range(1, n):
            temp = 0
            for j in range(i+1):
                temp += dp[i-j-1] * dp[j-1] if j - 1 >= 0 else dp[i-j-1]
            dp[i] = temp
        return dp[-1]