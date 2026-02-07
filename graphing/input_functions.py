def check_nan(input):
    try:
        float(input)
    except ValueError:
        return False
    else:
        return True

def check_empty(input):
    return bool(input)

def get_valid_position():
    """get a valid input, return 'None' when the loop should break"""
    while True:
        position = input("Enter Position: ")
        if position == 'x':
            return None
        elif check_nan(position) and check_empty(position) == True:
            return position
        else:
            print('please enter a valid number')

def get_valid_time(list):
    while True:
        time = input("Enter Time: ")
        if check_nan(time) and check_empty(time) and time not in list:
            return time
        else:
            print('please enter a valid number')

# def check_valid(input):
#     a = check_nan(input)
#     b = check_empty(input)
#     return input if a*b == 1 