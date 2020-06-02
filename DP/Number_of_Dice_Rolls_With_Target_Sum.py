'''
link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        memo = {}
        def recursion(d, f, t):
            if memo.get((d, f, t), False): 
                return memo[d, f, t]
            if t < d or d <= 0: return int(0)
            if d == 1 and t <= f: return int(1)
            res = 0
            for i in range(1, f + 1):
                res += recursion(d - 1, f, t - i)
                res %= (10 ** 9 + 7)
            
            memo[d, f, t] = res % (10 ** 9 + 7)
            return int(memo[d, f, t])
        return recursion(d, f, target)
    
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        dp = [[0] * (target + 1) for _ in range(d + 1)]
        
        for i in range(1, min(f + 1, target + 1)):
            dp[1][i] = 1
        
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k <= 0: break
                    dp[i][j] += dp[i - 1][j - k] % (10 ** 9 + 7)
                   
        return dp[-1][target] % (10 ** 9 + 7)
    
   