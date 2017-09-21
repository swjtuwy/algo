class Queue:

    def __init__(self, length):
        self.head = 0
        self.tail = 0
        self.length = length
        self.queue = [ None for i in range(self.length)]

    def enqueu(self, x):
        self.queue[self.tail] = x
        if self.tail == self.length:
            self.tail = 1
        self.tail += 1

    def dequeue(self):
        x = self.queue[self.head]
        if self.head == self.length:
            self.head = 1
        self.head += 1
        return x