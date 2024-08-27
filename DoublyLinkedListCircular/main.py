#20 and 17 to be done, with new list (17)
from pycparser.ply.ctokens import t_PLUSEQUAL
from sympy.codegen.fnodes import elemental
import numpy as np

class Node:
    def __init__(self, value):
        self.prev = None
        self.node = value
        self.next = None


class DCLinkedList:
    def __init__(self, value):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
            return
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.node.next = self.node
        self.node.prev = self.node
        self.length = 1

    def __str__(self):
        if self.head is None:
            return "Empty list that is"
        result = ""
        current = self.head
        while True:
            result += str(current.node) + " <-> "
            current = current.next
            if current == self.head:
                break
        return result[:-5]

    def prepend_element(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def backend_element(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def add_element(self, index, value):#Wherever
        if index == 0:
            self.prepend_element(value)
        if index == self.length - 1:
            self.backend_element(value)
        if index >= self.length:
            return -1
        new_node = Node(value)
        current = self.head
        for _ in range(index):
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

        if new_node.next == self.head:
            self.tail = new_node
        self.length += 1

    def traverse(self):
            current = self.head
            for i in range(self.length):
                print(f"{i}. element: {current.node}\n")
                current = current.next

    def reverse_traverse(self):
        current = self.tail
        for i in range(self.length):
            print(f"{i}. element: {current.node}\n")
            current = current.prev

    def search(self, value):
        current = self.head
        for index in range(self.length):
            if current.node == value:
                return index, current
            current = current.next

    def get(self, index):
        median = self.length
        if index <= median:
            current = self.head
            for _ in range(0, index):
                current = current.next
            return current
        elif index > median:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
            return current
        else:
            return -1

    def set(self, index, value):
        if index < 0 or index > self.length - 1:
            return -1
        elementt = self.get(index)
        elementt.node = value

    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        pop_element = self.head
        self.head = self.head.next
        pop_element.prev = None
        pop_element.next = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length -= 1

    def pop_last(self):
        to_pop = self.tail
        self.tail = self.tail.prev
        to_pop.next = None
        to_pop.prev = None
        self.head.prev = self.tail

    def remove(self):
        to_remove =

    # def remove_element(self):

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    DCLinkedList = DCLinkedList(3)
    print(DCLinkedList)
    DCLinkedList.add_element(0, 5)
    DCLinkedList.add_element(1, 8)
    print(DCLinkedList)
    DCLinkedList.prepend_element(493)
    print(DCLinkedList)
    DCLinkedList.backend_element(42)
    print(DCLinkedList)
    DCLinkedList.pop_first()
    DCLinkedList.pop_first()
    print(DCLinkedList)

    element = DCLinkedList.get(4)
    print(element.node)
    # DCLinkedList.traverse()
    # DCLinkedList.reverse_traverse()

    tp = DCLinkedList.search(3)
    print(tp)

    DCLinkedList.set(2, 1000)
    print(DCLinkedList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


