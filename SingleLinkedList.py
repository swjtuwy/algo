class LinkedList:

    class Node:

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None


    def isEmpty(self):
        return self.size == 0

    def push(self, x):
        self.head = self.Node(x, self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise 'stack is empty.'
        answer = self.head.value
        self.head = self.head.next
        self.size -= 1
        return answer

    def top(self):
        if self.isEmpty():
            return 'stack is empty.'
        return self.head.value

