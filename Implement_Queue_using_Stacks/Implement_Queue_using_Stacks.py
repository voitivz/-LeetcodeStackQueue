class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, ele):
        newNode = Node(ele)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            print("Hey! The stack is Empty")
            return None
        else:
            pop = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1
            return pop

    def top(self):
        if self.isEmpty():
            print("Hey! The stack is Empty")
            return None
        else:
            return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()

    def empty(self) -> bool:
        return self.stack1.isEmpty() and self.stack2.isEmpty()