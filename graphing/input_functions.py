def check_nan(i):
    """Check that the input is a number by attempting to turn it into a float.
    Returns True if it passes, False if it does not"""
    try:
        float(i)
    except ValueError:
        return False
    else:
        return True

def check_empty(i):
    """Check that the input is not empty by using the boolean function,
    returning True if it passes and False if it does not."""
    return bool(i)

def get_valid_position():
    """get a valid input, return 'None' when the loop should break, returns a
    valid floating point decimal"""
    while True:
        position = input("Enter Position: ")
        if position == 'x':
            return None
        #check for a valid input, and return it as a floating point
        elif check_nan(position) and check_empty(position):
            return float(position)
        else:
            print('please enter a valid number')

def get_valid_time(compare_against):
    """Gets a valid time input, also takes an argument for the list of times to
    compare it to, to ensure there are no duplicate time entries. Returns a valid
    floating point decimal"""
    while True:
        time = input("Enter Time: ")
        if check_nan(time) and check_empty(time):
            time = float(time)
            #make sure that the entry isn't already in the list
            if time in compare_against:
                print("time can't go backwards")
                #restart the loop if it is
                continue
            return float(time)
        else:
            print('please enter a valid number')