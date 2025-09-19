class Queue:
    def __init__(self):
        self.queue = []
        self.out = []

    def enqueue(self, value):
        self.queue.append(value)
        return self
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("CANT dequeue THE STACK IS EMPTY")
            return None
        else:
            self.out.append(self.queue[0])
            self.queue.pop(0)
        return self

    def front(self):
        if len(self.queue) == 0:
            print("THE STACK IS EMPTY")
        else:
            print(self.queue[0])
        return self




stack = Queue()

stack.front().dequeue().enqueue(10).enqueue(20).enqueue(30).enqueue(20).enqueue(20).enqueue(20).enqueue(20).enqueue(20).enqueue(20).front().dequeue().front()

