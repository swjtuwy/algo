class CircularQueue:

    # TODO complete CircularQueue
    class Node:

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.size = 0
        self.tail = None

    def isEmpty(self):
        return self.size == 0




