'''
link: https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

'''
from collections import deque


class Solution:
    def reverse(self, x: int) -> int:
        
        sign, res = 1 if x >= 0 else -1, 0
        x = abs(x)
        
        queue = deque([])
        for n in range(31, -1, -1):
            queue.append(x // 10 ** n)
            x %= 10 ** n
            
        while queue and queue[0] == 0:
            queue.popleft()
            
        while queue:
            ele = queue.popleft()
            res += ele * 10 ** n
            n += 1
            
        return sign * res if res < 2 ** 31 and res >= -2 ** 31 else 0 