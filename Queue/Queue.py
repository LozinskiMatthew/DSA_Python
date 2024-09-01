class Queue:
    def __init__(self, capacity):
        self.length = capacity
        self.items = capacity * [None]
        self.end = -1
        self.start = -1

    def __str__(self):
        stringed = []
        for i in range(len(self.items)):
            curr = self.items[self.start]
            stringed.append(curr)
            curr = curr + i + 1
        return ", ".join(stringed)

    def isEmpty(self):
        if self.start == -1 and self.end == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.items[self.end + 1] == self.items[self.start]:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isEmpty():
            self.items[self.start] = value
            self.items[self.end] = value

        elif self.isFull():
            return "Queue is already filled!!!"

        elif self.end + 1 == self.length:
            self.items[0] = value
            self.end = 0
        else:
            self.items[self.end + 1] = value
