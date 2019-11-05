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

class MyCircularQueue(object):
    '''Array Two pointer'''
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [-1] * k
        self.k = k
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.tail + 1 < self.k:
            if self.tail + 1 != self.head:
                self.tail += 1
                if self.head == -1:
                    self.head = self.tail
            else:
                return False
        elif self.head > 0:
            self.tail = 0
        else:
            return False
        
        self.queue[self.tail] = value
        return True
       
        
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue[self.head] != -1:
            self.queue[self.head] = -1
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            elif self.head + 1 < self.k:
                self.head += 1
            else:
                self.head = 0
            return True
        else:
        
            return False
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.queue[self.head]
       

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.queue[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.tail + 1 < self.k:
            if self.tail + 1 == self.head:
                return True
            else:
                return False
        elif self.head > 0:
            return False
        else:
            return True