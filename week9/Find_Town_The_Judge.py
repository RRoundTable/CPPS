'''
link: https://leetcode.com/problems/find-the-town-judge/

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''O(N^2)/O(N^2)'''
        d = defaultdict(lambda: {}) 
        for a, b in trust:
            d[a][b] = False

        for a in range(1, N+1):
            if d[a] == {}:
                count = 0
                for j in range(1, N + 1):
                    if a == j: continue
                    if d[j].get(a, True):break
                    else:
                        count += 1
                if count == N - 1:
                    return a
        return -1
    
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''O(N)/O(N)'''
        count1, count2 = defaultdict(lambda: 0), defaultdict(lambda:0)
        for a, b in trust:
            count1[a] += 1
            count2[b] += 1
        for i in range(1, N + 1):
            if count1[i] == 0 and count2[i] == N - 1:
                return i
        return -1
        
        
        