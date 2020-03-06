'''
link: https://leetcode.com/problems/friend-circles/
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''

from collections import defaultdict


class Solution:
    '''O(N^2)/O(N)'''
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        N, visited, edges, count = len(M), set(), defaultdict(list), 0
        
        for i in range(N):
            for j in range(N):
                if M[i][j] and i != j: edges[i].append(j)

        for start in range(N):
            if start in visited: continue
            stack = [start]
            while stack:
                node = stack.pop()
                if node in visited: continue
                for ne in edges[node]:
                    stack.append(ne)
                visited.add(node)
            count += 1

        return count
        
        
        
class Solution:
    '''O(NlogN)/O(N)'''
    def findCircleNum(self, M: List[List[int]]) -> int:       
        sets, N = [i for i in range(len(M))], len(M)
        
        def find(i):
            if i == sets[i]: 
                return i
            sets[i] = find(sets[i])
            return sets[i]
            
        def union(i, j):
            i, j = find(i), find(j)
            sets[i] = j
        
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j]: 
                    union(i, j)

        return len(set(find(u) for u in sets))