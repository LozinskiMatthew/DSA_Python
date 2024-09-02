import Queue

if __name__ == "__main__":
    q = Queue.Queue(4)
    # print(q.isEmpty())
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(q.isFull())
    # print(q.start)
    # print(q.end)
    print(q)
    q.dequeue()
    print(q)




