"""MAJOR NOTE! THIS IS NOT ACTUALLY EVEN CLOSE TO RIGHT, EACH SYMBOL NEEDS
ITS OWN STACK, AND ADDITIONAL LOGIC FOR QUOTES, RAN OUT OF TIME WILL HAVE TO 
FIX LATER!"""

"""New note, that is not the best way to do it, use one stack with a function that
check if the symbol is correct. Ran out of time again :("""

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
                stack.pop()
            else:
                return False
        
        elif i == '"' and stack.size() % 2 == 0:
            stack.push(i)

        
    return stack.is_empty()

def matches(left_symbol, right_symbol):
    left = "([{"
    right = ")]}"
    return left.index == right.index

print(check_symbols('()(())()()()()()'))

