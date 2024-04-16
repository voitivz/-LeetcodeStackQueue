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

class FreqStack:

    def __init__(self):
        self.freq_map = {} 
        self.freq_stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:

        self.freq_map[val] = self.freq_map.get(val, 0) + 1
        freq = self.freq_map[val]

        self.max_freq = max(self.max_freq, freq)

        if freq not in self.freq_stacks:
            self.freq_stacks[freq] = Stack()
        self.freq_stacks[freq].push(val)

    def pop(self) -> int:

        val = self.freq_stacks[self.max_freq].pop()

        self.freq_map[val] -= 1

        if self.freq_stacks[self.max_freq].isEmpty():
            self.max_freq -= 1
        return val