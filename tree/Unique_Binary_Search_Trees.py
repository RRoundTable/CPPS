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
 

Constraints:

1 <= n <= 19
'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (max(3, n + 1)); dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = sum(dp[i - 1 - k] * dp[k] for k in range(i))
        return dp[n]