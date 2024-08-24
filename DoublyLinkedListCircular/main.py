# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
        else:
            self.node = Node(value)
            self.head = self.node
            self.tail = self.node
            self.node.next = self.node
            self.node.prev = self.node

    def __str__(self):
        if self.head is None:
            return "Empty list that is"
        result = ""
        current = self.head
        while True:
            result += str(current.node) + " -> "
            current = current.next
            if current == self.head:
                break
        return result[:-4]

    def add_element(self, index, value):
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
