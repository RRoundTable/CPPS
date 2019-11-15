'''
link: https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

'''




# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


from collections import defaultdict


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = defaultdict(lambda: None)
        stack = [node]
        visited = []
        while stack:
            pop = stack.pop()
            if pop in visited:
                continue
            d[pop] = Node(pop.val, [])
            visited.append(pop)
            for n in pop.neighbors:
                stack.append(n)

        stack = [node]
        visited = []
        while stack:
            pop = stack.pop()
            if pop in visited:
                continue
            visited.append(pop)
            for n in pop.neighbors:
                d[pop].neighbors.append(d[n])
                stack.append(n)

        return d[node]


from collections import defaultdict


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = defaultdict(lambda: None)
        stack = [node]
        visited = []
        while stack:
            pop = stack.pop()
            if pop in visited:
                continue
            if pop not in d:
                d[pop] = Node(pop.val, [])
            visited.append(pop)
            for n in pop.neighbors:
                stack.append(n)
                if n not in d:
                    d[n] = Node(n.val, [])
                d[pop].neighbors.append(d[n])
        return d[node]

