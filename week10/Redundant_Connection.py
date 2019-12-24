'''
link: https://leetcode.com/problems/redundant-connection/
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
'''

from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connected = defaultdict(lambda: set()), []
        for u, v in edges:
            prev = connected[v]
            connected[v] = connected[v] | connected[u]
            if u in connected[v] or prev & connected[u]:
                return [u, v]
            connected[v].add(u); 
            temp = set()
            for u in connected[v]:
                temp = temp | connected[u]  
                connected[u] = temp | connected[v] | {v}
                connected[u] = connected[u] - {u}

                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''union-find'''
        connected, union = {}, defaultdict(lambda: set())
        for u, v in edges:
            connected[u], connected[v], union[u], union[v] = u, v, {u}, {v}
        for u, v in edges:
            if connected[u] != connected[v]:
                total = union[connected[u]] | union[connected[v]]
                head = min(connected[v], connected[u])
                for node in total:
                    connected[node] = head
                    union[head] = union[head] | {node}                
            else:
                return u, v
            
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''union-find'''
        union = list(range(len(edges) + 1))
        def find(x):
            while x != union[x]:
                x = union[x]
            return x
        for u, v in edges:
            uu, uv = find(u), find(v)
            if uu == uv: return [u, v]
            union[uu], union[uv] = min(uu, uv), min(uu, uv)
            
            