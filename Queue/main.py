from torch.onnx.symbolic_opset13 import quantized_linear

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


    ll = Queue.LL(5)

    # print(ll)

    # print(ll.isEmpty())

    print("\n\n")
    ql = Queue.QueueList(5)

    ql.enqueue(6)
    ql.enqueue(7)

    print("Dequeued value:", ql.dequeue())  #It prints None, there is a bug in the code

    print(ql)

