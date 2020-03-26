'''
link: https://leetcode.com/problems/critical-connections-in-a-network/
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

'''

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ans, edges, level, low, visited = [], defaultdict(list), [None for _ in range(n)], [None for _ in range(n)], [None for _ in range(n)]
        
        for a, b in connections:
            edges[a].append(b); edges[b].append(a)
        
        cur, start, self.cur = 0, 0, 0
        
        def dfs(node, parent):
            if level[node] is None:
                level[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in edges[node]:
                    if level[n] is None:
                        dfs(n, node)
                if parent is not None:
                    l = min([low[i] for i in edges[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in edges[node]+[low[node]])
                low[node] = l
            
        dfs(0, None)
        
        for u, v in connections:
            if low[u] > level[v] or low[v] > level[u]: ans.append([u, v])
        return ans
   
        
      


        
