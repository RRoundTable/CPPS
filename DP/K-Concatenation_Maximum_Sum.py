'''
link: https://leetcode.com/problems/k-concatenation-maximum-sum/

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
'''
class Solution:
    '''
    Brute-Force
    O((N*K)^2)/O(1)
    '''
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        arr = arr * k
        n = len(arr)
        res = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                res = max(res, s)
        return res % (10 ** 9 + 7)
    
class Solution:
    '''
    Dynamic Programming
    O(NK)/O(NK)
    '''
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        arr = arr * k
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(arr[i], dp[i-1] + arr[i] if i > 0 else 0)
        return max(dp)
    
from itertools import chain
class Solution:
    '''
    Dynamic Programming and Iterative
    
    '''
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        s, n, res = sum(arr), len(arr), 0
        
        dp, cum = [0] * n, [0] * n
        dp[0], cum[0] = arr[0], arr[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
            cum[i] = arr[i] + cum[i-1]
        
        max_subarray = max(dp)
        
        if s > 0:
            res = max_subarray + s * (k-1)
        else:
            res = max(dp[-1] + max(cum), max_subarray)
            
        return max(res, 0) % (10 ** 9 + 7)
        