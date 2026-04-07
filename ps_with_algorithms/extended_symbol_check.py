"""MAJOR NOTE! THIS IS NOT ACTUALLY EVEN CLOSE TO RIGHT, EACH SYMBOL NEEDS
ITS OWN STACK, AND ADDITIONAL LOGIC FOR QUOTES, RAN OUT OF TIME WILL HAVE TO 
FIX LATER!"""

from stack_as_list import Stack

def check_symbols (string):
    """this is an extended version of the previous parenthese checker that
    is adapted to handle various other symbols"""
    string = list(string)
    stack = Stack()
    for i in string:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                return False
        
        elif i == '{':
            stack.push(i)
        elif i == '}':
            if not stack.is_empty():
                stack.pop()
            else:
                return False

        elif i == '[':
            stack.push(i)
        elif i == ']':
            if not stack.is_empty():
                stack.pop()
            else:
                return False
            
        elif i == '"' and stack.size() % 2 == 0:
            stack.push(i)

        
    return stack.is_empty()

print(check_symbols('()(())()()()()()'))

