'''
link: https://leetcode.com/problems/coin-change/
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans, dp = float('inf'), {}
        def backtracking(remain):
            if dp.get(remain, False): 
                return dp[remain]
            if remain < 0: return float('inf')
            if remain == 0: return 1
            for coin in coins:
                res = backtracking(remain - coin) + 1
                dp[remain] = min(res, dp.get(remain, float('inf')))
            return dp.get(remain, float('inf'))
        ans = backtracking(amount)
        return ans - 1 if ans < float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {coin:1 for coin in coins}; dp[0] = 0
        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0 and dp.get(num - coin, -1) >= 0:
                    # print(num, num - coin, dp[num - coin])
                    dp[num] = min(dp[num - coin] + 1, dp.get(num, float('inf')))
        return dp[amount] if dp.get(amount, -1) >= 0 else - 1