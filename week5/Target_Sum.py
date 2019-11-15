'''
link: https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        sums = [ele for ele in range(-total, total + 1)]
        dp = [[0] * 2001 for ele in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        
        for i in range(1, len(nums)):
            for sums in range(-1000, 1001):
                if dp[i - 1][sums + 1000] > 0:
                    dp[i][nums[i] + sums + 1000] += dp[i - 1][sums + 1000]
                    dp[i][-nums[i] + sums + 1000] += dp[i - 1][sums + 1000]
        return 0 if S > 1000 else dp[-1][S + 1000]
            
            
        
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [0] * 2001
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        
        for i in range(1, len(nums)):
            new = [0] * 2001
            for sums in range(-1000, 1001):
                if dp[sums + 1000] > 0:
                    new[nums[i] + 1000 + sums] += dp[sums + 1000]
                    new[-nums[i] + 1000 + sums] += dp[sums + 1000]
            dp = new
        
        return 0 if S > 1000 else dp[1000 + S]
    
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cashe = {}
        # memorization
        def find(i, s):
            print(self.cashe)
            if (i, s) not in self.cashe:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = find(i + 1, s - nums[i]) + find(i + 1, s + nums[i])
                self.cashe[(i, s)] = r
            return self.cashe[(i, s)]
    
        return find(0, S)