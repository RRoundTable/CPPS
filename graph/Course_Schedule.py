'''
link: https://leetcode.com/problems/course-schedule/
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''
from collections import defaultdict


class Solution:
    '''O(|V|)/O(|E|)'''
    def canFinish(self, num: int, prerequisites: List[List[int]]) -> bool:
        color, edges, is_possible = {}, defaultdict(list), True
        
        for end, start in prerequisites:
            edges[start], color[start], color[end] = edges[start] + [end], 0, 0
        
        def dfs(node):
            nonlocal is_possible
            if color[node] == 2: return True
            color[node] += 1
            res = True
            for ne in edges[node]:
                if color[ne] == 0: dfs(ne)
                if color[ne] == 1: is_possible = False
            color[node] = 2
        
        for i in range(num):
            if color.get(i, -1) == 0: dfs(i)
        return is_possible