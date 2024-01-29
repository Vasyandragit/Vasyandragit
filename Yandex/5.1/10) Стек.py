class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return not self.items
    
    def pop(self):
        return self.items.pop()

stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())