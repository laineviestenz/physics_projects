from stack_as_list import Stack

def check_symbols (string):
    """this is an extended version of the previous parenthese checker that
    is adapted to handle various other symbols"""
    string = list(string)
    stack = Stack()
    for i in string:
        if i in '({[':
            stack.push(i)
        elif i in '}])':
            if not stack.is_empty():
                if matches(stack.peek(), i):
                    stack.pop()
                else:
                    return False        
    return stack.is_empty()

def matches(left_symbol, right_symbol):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    return left.index(left_symbol) == right.index(right_symbol)

print(check_symbols('()[]'))