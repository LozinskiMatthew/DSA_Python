class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LL:
    def __init__(self, value=None):
        if value = None:
            self.head = None
            self.tail = None
            self.length = 0
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        if self.head == None:
            return "Empty!"
        curr = self.head
        stringed = []
        stringed.append(str(curr.value))
        while curr != tail:
            curr = curr.next
            stringed.append(str(curr.value))
        stringed.append(str(curr.value))
        return ", ".join(stringed)

    def isEmpty(self):
        if self.head == None:
            True
        else:
            False


class QueueList:

    def __init__(self, nd=None):
        self.ll = LL(nd)
        if ll.isEmpty():




class Queue:
    def __init__(self, capacity):
        self.length = capacity
        self.items = capacity * [None]
        self.end = -1
        self.start = -1

    def __str__(self):
        stringed = []
        if self.isEmpty():
            return "Queue is empty"
        curr = self.items[self.start]
        helper = self.start
        while curr is not None:
            if helper == self.length - 1 and self.end != self.length - 1:
                helper = 0
                stringed.append(str(self.items[0]))
            stringed.append(str(curr))
            helper += 1
            if helper == self.length - 1:
                stringed.append(str(self.items[self.length - 1]))
                break
            curr = self.items[helper]
        return ", ".join(stringed)

    def isEmpty(self):
        if self.start == -1 and self.end == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.end + 1 == self.length and self.start == 0:
            return True
        elif self.end + 1 == self.start and self.start != 0:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isEmpty():
            self.end = 0
            self.start = 0
            self.items[self.start] = value
            self.items[self.end] = value

        elif self.isFull():
            return "Queue is already filled!!!"

        elif self.end + 1 == self.length:
            self.items[0] = value
            self.end = 0
        else:
            self.items[self.end + 1] = value
            self.end += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"

        self.items[self.start] = None
        if self.start == self.length - 1:
            self.start = 0
            return
        self.start += 1
