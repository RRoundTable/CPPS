'''
link: https://leetcode.com/problems/design-circular-queue/
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = 0
        self.k = k
        self.dummy = self.head = Node('head')
        self.tail = Node('tail')
        self.head.next, self.tail.prev = self.tail, self.dummy
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size < self.k:
            node = Node(value)
            self.head.next, self.tail.prev = node, node
            node.next, node.prev = self.tail, self.head
            self.head = self.head.next
            self.size += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.size -= 1
        remove_node = self.dummy.next
        self.dummy.next, remove_node.next.prev = remove_node.next, self.dummy
        if self.head == remove_node:
            self.head = self.dummy
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.dummy.next.value if self.size > 0 else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.prev.value if self.size > 0 else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.k
