'''
link: https://leetcode.com/problems/course-schedule-iii/
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 

Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

'''
class Solution:
    '''O(MD)/O(MD)'''
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        memo = [[None] * (courses[-1][1] + 1) for _ in range(len(courses))]
        
        def schedule(i, time):
            nonlocal courses, memo
            if i == len(courses): return 0;
            if memo[i][time]: 
                return memo[i][time]
            
            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken = 1 + schedule(i+1, time + courses[i][0])
            
            not_taken = schedule(i+1, time)
            memo[i][time] = max(taken, not_taken)
            return memo[i][time]
        
        return schedule(0, 0)
    
class Solution:
    '''iterative'''
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        time, ans = 0, 0
        for i, (t, d) in enumerate(courses):
            if time + t <= d:
                time += t; 
                courses[ans] = courses[i]
                ans += 1
            else:
                max_i = i
                for j in range(ans):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                    courses[max_i] = courses[i]
        return ans
    
from heapq import heappop, heappush, heapify


class Solution:
    '''priority queue'''
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        start = 0
        remain = []
        for t, end in sorted(courses, key=lambda x: x[1]):
            start += t
            heappush(remain, -t)
            while start > end:
                start += heappop(remain)
        return len(remain)
  
            
            
        