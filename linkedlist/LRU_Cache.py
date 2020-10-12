'''
link: https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.time = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key][1] = self.time
            self.time += 1
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = [value, self.time]
        self.time += 1
        if len(self.cache) > self.capacity:
            min_t = float('inf')
            for k, (v, t) in self.cache.items():
                if min_t > t:
                    min_t = t
                    min_key = k
            self.cache.pop(min_key)
          
        
class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = LinkedList('head', None)
        self.tail = LinkedList('tail', None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_end(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        tail_prev = self.tail.prev
        self.tail.prev, tail_prev.next = node, node
        node.next, node.prev = self.tail, tail_prev
 
        
    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.move_to_end(node)
            return self.hash[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key not in self.hash:
            node = LinkedList(key, value)
            tail_prev = self.tail.prev
            tail_prev.next, self.tail.prev = node, node
            node.next, node.prev = self.tail, tail_prev
            self.hash[key] = node
            if len(self.hash) > self.capacity:
                remove_node = self.head.next
                self.hash.pop(remove_node.key)
                next_node = self.head.next.next
                self.head.next, next_node.prev = next_node, self.head
                del(remove_node)
        else:
            self.hash[key].value = value
            self.move_to_end(self.hash[key])
