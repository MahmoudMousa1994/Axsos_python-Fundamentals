class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) <= 10:
            self.stack.append(value)
        else:
            print("THE STACK IS FULL")
        return self
    

    def pop(self):
        if len(self.stack) == 0:
            print("CANT POP THE STACK IS EMPTY")
        else:
            self.stack.pop()
        return self

    def peek(self):
        if len(self.stack) == 0:
            print("THE STACK IS EMPTY")
        else:
            print(self.stack[len(self.stack) - 1])
        return self




stack = Stack()

stack.peek().pop().push(10).push(20).push(30).push(20).push(20).push(20).push(20).push(20).push(20).push(20).push(20).push(20).push(20).push(20).push(20).peek().pop().peek()

