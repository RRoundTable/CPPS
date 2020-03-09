'''
link: https://leetcode.com/problems/network-delay-time/
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

'''
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    '''O(N^2 + E)/O(N+E)'''
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        Q, edges, dist = set(), defaultdict(dict), {K:0}
        
        for u, v, w in times:
            edges[u][v] = w; Q.add(u); Q.add(v)

        while Q:
            u = min(Q, key=lambda x: dist.get(x, float('inf')))
            Q.remove(u)
            for ne in edges[u]:
                if ne not in Q: continue
                alt = dist.get(u, float('inf')) + edges[u].get(ne, float('inf'))
                if alt < dist.get(ne, float('inf')):
                    dist[ne] = alt
        return max(dist.values()) if len(dist) == N else -1
    
    
class Solution:
    '''O(N^2 + E)/O(N+E)'''
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        Q, edges, dist = [(0, K)], defaultdict(list), {}
        for u, v, w in times:
            edges[u].append((v, w))
        while Q:
            d1, u = heappop(Q)
            if u in dist: continue
            dist[u] = d1
            for ne, d2 in edges[u]:
                if ne not in dist:
                    heappush(Q, (d1 + d2, ne))
        return max(dist.values()) if len(dist) == N else -1
        