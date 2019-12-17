'''
link:https://leetcode.com/problems/partition-array-for-maximum-sum/
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
'''
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''O(A*K^2)/O(K)'''
        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            for j in range(1, min(K + 1, i + 1)):
                dp[i] = max(dp[i], dp[i-j] + max(A[i-j:i]) * j) 
        return dp[-1]
    
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''O(A * K)/O(A)'''
        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            maxval = 0
            for j in range(1, min(K + 1, i + 1)):
                maxval = max(maxval, A[i-j])
                dp[i] = max(dp[i], dp[i-j] + maxval * j) 
        return dp[-1]
