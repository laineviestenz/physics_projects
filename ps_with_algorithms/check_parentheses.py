from stack_as_list import Stack

def check_parentheses (string):
    """new method will use stacks for a much cleaner solution than I was
    previously working on."""
    """If there is a left parenthese, push it to the stack if there is a right
    parenthese, pop from the stack. After going through the entire list, check
    if the stack is empty. Also, if the stack is empty before the end, return 
    false"""
    string = list(string)
    stack = Stack()
    for i in string:
        if i == '(':
            stack.push(i)
        if i == '(':
            if not stack.is_empty():
                stack.pop(i)
            else:
                return False
    return stack.is_empty()

print(check_parentheses('(0)()())(())'))

