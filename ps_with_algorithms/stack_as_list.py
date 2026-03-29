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
        "check but do not remove"
        return self.stack[-1]
    
    def is_empty(self):
        "check if list is empty"
        return not bool(self.stack)
    
    def size(self):
        "return the size of the list"
        return len(self.stack)
    
my_stack = Stack()
my_stack.push('cheese')