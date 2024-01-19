class QueueArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from empty queue")

    def size(self):
        return len(self.items)
