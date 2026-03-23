class Stack():
    """implement a stack as a list
    inspired by PSwAaDSUP"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return bool(self.stack)
    
    def size(self):
        return len(self.stack)
    
my_stack = Stack()
my_stack.push('cheese')