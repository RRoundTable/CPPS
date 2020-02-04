'''
link: https://leetcode.com/problems/task-scheduler/
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

'''

from collections import Counter
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alpha, ans = [0]  * 26, 0
        for ele in tasks:
            alpha[ord(ele) - ord('A')] += 1
        alpha.sort()
        while alpha[-1] > 0:
            for i in range(n+1):
                if alpha[25] == 0: break
                if i < 26 and alpha[25-i] > 0:
                    alpha[25-i] -= 1
                ans += 1
            alpha.sort()
        return ans
    
    
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alpha, ans = [0]  * 26, 0
        for ele in tasks:
            alpha[ord(ele) - ord('A')] -= 1
        while alpha[0] < 0:
            save = []
            for i in range(n+1):
                if save and save[0] == -1: break
                if alpha:
                    top = heappop(alpha)
                    save.append(top)
                ans += 1
            for top in save:
                heappush(alpha, min(top + 1, 0))
        return ans
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = sorted(Counter(tasks).values())
        maxval = count.pop()
        ans = (maxval - 1) * (n + 1) + 1 
        idle = ans - maxval
        for c in count:
            if c < maxval: idle -= c
            else:
                idle, ans = idle - (c - 1), ans + 1
        return ans - idle if idle <= 0 else ans