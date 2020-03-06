'''
link:https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

'''

from collections import defaultdict
from typing import List


class Solution:
    '''O(E^d)/O(E)'''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        count, edges, N = defaultdict(int), defaultdict(list), len(tickets)
        for start, end in tickets:
            count[(start, end)] += 1
            edges[start].append(end)
        
        for start, _ in tickets:
            edges[start] = sorted(edges[start])
        
        def dfs(node, path=[]):
            path.append(node)
            if len(path) == N + 1: return path
            for v in edges[node]:
                if not count[node, v]: continue
                count[node, v] -= 1
                res = dfs(v, path)
                if len(res) == N + 1: return res
                count[node, v] += 1; path.pop()
            return path
        return dfs('JFK')


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges, N = defaultdict(list), len(tickets)
        for start, end in sorted(tickets, reverse=True):
            edges[start].append(end)
        path, i = [None] * (N + 1), N
        def visit(node):
            nonlocal i
            while edges[node]:
                visit(edges[node].pop())
            path[i] = node; i -= 1
        visit('JFK')
        return path
           
           
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges, N = defaultdict(list), len(tickets)
        for start, end in sorted(tickets, reverse=True):
            edges[start].append(end)
        path, i, stack, visited = [None] * (N + 1), N, ['JFK'], set()
        while stack:
            while edges[stack[-1]]:
                stack += edges[stack[-1]].pop(),
            path[i] = stack.pop(); i -= 1
        return path