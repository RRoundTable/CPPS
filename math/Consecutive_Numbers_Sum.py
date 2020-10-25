'''
link: https://leetcode.com/problems/consecutive-numbers-sum/
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
'''


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        for i in range(2, N):
            q, r = divmod(N, i)
            if i % 2 == 0 and r == i // 2 and q >= r and q > 0:
                count += 1
            if i % 2 == 1 and r == 0 and q > i // 2:
                count += 1
        return count
    
    
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        i = 3
        while N % 2 == 0:
            N //= 2
        
        while i * i <= N:
            count = 0
            while N % i == 0:
                count += 1
                N /= i
            res *= (count + 1)
            i += 2
            
        return res if N == 1 else res * 2