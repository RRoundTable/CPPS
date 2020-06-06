'''

link: https://leetcode.com/problems/flower-planting-with-no-adjacent/
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.

'''

from collections import defaultdict

class Solution:
    '''O(N)/O(N)'''
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        d, visited, ans = defaultdict(list), set(), [1] * (N + 1)

        for x, y in paths:
            d[x].append(y); d[y].append(x)
        
        # bfs
        for i in d.keys():
            if i in visited: continue
            remain = {1, 2, 3, 4} - {ans[garden] for garden in d[i] if garden in visited}
            ans[i] = remain.pop()
            visited.add(i)
        return ans[1:]
        
        