'''
link: https://leetcode.com/problems/evaluate-division/
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

from collections import defaultdict
import itertools 


class Solution:
    '''O(MN)/O(N^2)'''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weight, edges, u = {tuple(eq): w for eq, w in zip(equations, values)}, defaultdict(list), {}
        for (a, b), v in zip(equations, values):
            weight[b, a] = 1/v
            weight[a, a], weight[b, b] = 1, 1
            
        for start, end in equations:
            edges[start].append(end)
            edges[end].append(start)
            u[start], u[end] = start, end
        
        def union(a, b):
            a, b = find(a), find(b)
            u[a] = b
        
        def find(a):
            if a == u[a]: return a
            u[a] = find(u[a])
            return u[a]
        
        def dfs(node):
            if node in visited: return
            path.append(node); visited.add(node)
            if node == B: return True
            for ne in edges[node]:
                if dfs(ne): return True
            path.pop()
            
        for start, end in equations:
            union(start, end)
            
        ans = []
        for A, B in queries:
            if not u.get(A, False) or not u.get(B, False) or (A != B and find(A) != find(B)):
                ans.append(-1.0); continue;      
            if weight.get((A, B), float('-inf')) > float('-inf'): ans.append(weight[A, B]); continue
            visited, path, val = set(), [], 1
            dfs(A)
            for i in range(len(path) - 1):
                a, b = path[i], path[i+1]
                val *= weight[a, b]
            ans.append(val)
        return ans


class Solution:
    '''O(N^3)/O(N^2)'''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weight, ans, vertexs = defaultdict(dict), [], set()
        for (a, b), v in zip(equations, values):
            weight[a][a] = weight[b][b] = 1
            weight[a][b], weight[b][a] = v, 1/ v
        for k, i, j in itertools.permutations(weight, 3):
            if k in weight[i] and j in weight[k]:
                weight[i][j] = weight[i][k] * weight[k][j]
        return [weight[a].get(b, -1.0) for a, b in queries] 