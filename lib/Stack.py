class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full. Cannot push more items.")

    def pop(self):
        if self.isEmpty():
            return None  # Return None if stack is empty
        return self.items.pop()  # Remove and return the last item

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot peek from an empty stack.")
        return self.items[-1]  # Return the last item without removing it

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if self.isEmpty():
            return -1
        try:
            index = self.items.index(target)
            return len(self.items) - index - 1
        except ValueError:
            return -1
