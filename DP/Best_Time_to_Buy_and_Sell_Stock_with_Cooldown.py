'''
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Say you have an a rray for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
class Solution:
    '''O(N)/O(1)'''
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        for p in prices:
            sold, held, reset = held + p, max(reset - p, held), max(reset, sold) 
        return max(sold, held, reset)
    
class Solution:
    '''O(N^2)/O(N)'''
    def maxProfit(self, prices: List[int]) -> int:
        d = [0] * len(prices)
        for i in reversed(range(len(prices))):
            d[i] = d[i+1] if i + 1 < len(prices) else d[i]
            for j in range(i, len(prices)):
                after = d[j+2] if j + 2 < len(prices) else 0
                d[i] = max(d[i], max(prices[j] - prices[i], 0) + after)
        return d[0] if prices else 0 
        