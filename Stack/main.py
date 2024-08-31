class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ll: #You must provide atleast one element within the list
    def __init__(self, value=None):
        if value == None:
            self.head = None
            self.tail = None
            self.length = 0
            return
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __str__(self):
        if self.head is None:
            return "Empty stack"
        curr = self.head
        return_string = str(curr.value) + " -> "
        while curr != self.tail:
            curr = curr.next
            return_string += str(curr.value) + " -> "
        return return_string[:-4]


class list_stack:
    def __init__(self, llist):
        self.list = llist

    def __str__(self):
        result = self.list.__str__()
        return result

    def isEmpty(self):
        if self.list.head is None:
            return True
        else:
            return False

    def push(self, value):
        if self.isEmpty():
            return "List is empty"
        new_node = Node(value)
        new_node.next = self.list.head
        self.list.head = new_node
        self.list.length += 1

    def pop(self):
        if self.isEmpty():
            return "List is empty"
        to_pop = self.list.head
        self.list.head = self.list.next
        to_pop.next = None
        self.list.length -= 1

    def peek(self):
        if self.isEmpty():
            return "List is empty"
        return self.list.head.value

    def delete_stack(self):
        self.list.head = None
        self.list.tail = None



'''

class Stack:  # From list
    def __init__(self):
        self.list = []

        def __str__(self):
            values = [str(x) for x in self.list]
            return "\n".join(values)

    def push(self, value):
        self.list.append(value)

    def pop(self):
        self.list.pop()

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def delete(self):
        self.list = None

    def peek(self):
        if self.isEmpty():
            return "The list does not contain any elements."
        return self.list[0]

'''

if __name__ == "__main__":
    # st = Stack()
    # print(st.list)
    linked_list = ll(20)
    print(linked_list)
    list_stack = list_stack(linked_list)
    print(list_stack.peek())
    list_stack.push(30)
    # print(list_stack.__str__())
    print(list_stack.peek())
    print(list_stack)


