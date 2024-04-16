class Node(object):
  def __init__(self, item=None):
    self.item = item
    self.next = None
    self.previous = None

class Queue(object):
    def __init__(self):
        """post: creates an empty FIFO queue"""
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, x):
        """post: adds x at back of queue"""
        newNode = Node(x)
        newNode.next = None
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.length += 1

    def dequeue(self):
        """pre: self.size() > 0
           post: removes and returns the front item"""
        item = self.head.item
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def front(self):
        return self.head.item if self.head else None

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0


class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        while not self.queue1.isEmpty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(x)
        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self) -> int:
        return self.queue1.dequeue()

    def top(self) -> int:
        return self.queue1.front()

    def empty(self) -> bool:
        return self.queue1.isEmpty()

