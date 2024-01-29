class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def is_empty(self):
        return not self.items
    
    def pop(self):
        return self.items.pop()
