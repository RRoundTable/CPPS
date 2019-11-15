'''
link: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        for i in range(2, n):
            if i ** 2 <= n:
                nums.append(i ** 2)
        queue = {n}
        cnt = 0
        while queue:
            cnt += 1
            temp = set()
            for pop in queue:
                for ele in nums:
                    if ele == pop:
                        return cnt
                    elif ele > pop:
                        break
                    else:
                        temp.add(pop - ele)
            queue = temp