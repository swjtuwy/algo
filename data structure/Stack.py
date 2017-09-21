class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return False
        return True

    def push(self):
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.isEmpty():
            raise 'underflow'
        self.top -= 1
        return self.stack[self.top]