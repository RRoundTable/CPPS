'''
link: https://leetcode.com/problems/flatten-nested-list-iterator/
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''

from collections import deque


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.que = deque(self.flatten(nestedList))
  
    def flatten(self, nestedlist):
        f = []
        for ele in nestedlist:
            if ele.isInteger(): f.append(ele.getInteger())
            else: f += self.flatten(ele.getList())
        return f
        
    def next(self) -> int:
        return self.que.popleft()
    
    def hasNext(self) -> bool:
        return len(self.que) 


class NestedIterator(object):

    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)

    def next(self):
        return self.value

    def hasNext(self):
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False