'''
link: https://leetcode.com/problems/interleaving-string/
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''


from collections import defaultdict


class Solution:
    '''Memorization
    O(MN)/O(MN)
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = defaultdict(lambda: False)
        s1, s2, s3 = "a" + s1, "a" + s2, "aa" + s3
        def recursion(i, j, k):
            if memo[i, j]: return memo[i, j]
            if k == len(s3): return i == len(s1) and j == len(s2)
            if s3 and s1 and i < len(s1) and s3[k] == s1[i]: memo[i, j] = memo[i, j] or recursion(i+1, j, k + 1)
            if s3 and s2 and j < len(s2) and s3[k] == s2[j]: memo[i, j] = memo[i, j] or recursion(i, j + 1, k + 1)
            return memo[i, j]
        return recursion(0, 0, 0)
    

class Solution:
    '''2D dynamic programing
    O(MN)/O(MN)
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1, s2, s3 = "a" + s1, "a" + s2, "aa" + s3
        n, m = len(s1), len(s2)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        if len(s3) != n + m: return False
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0: dp[i][j] = True
                elif i == 0: dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0: dp[i][j] = dp[i-1][j] and s1[i-1] ==s3[i+j-1] 
                else:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] ==s3[i+j-1])
        return dp[-1][-1]
    
    
class Solution:
    '''1D dynamic programing
    O(MN)/O(M)
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1, s2, s3 = "a" + s1, "a" + s2, "aa" + s3
        n, m = len(s1), len(s2)
        dp = [False] * (m+1)
        if len(s3) != n + m: return False
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0: dp[i] = True
                elif i == 0: dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0: dp[j] = dp[j] and s1[i-1] ==s3[i+j-1] 
                else:
                    dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] ==s3[i+j-1])
        return dp[-1]


