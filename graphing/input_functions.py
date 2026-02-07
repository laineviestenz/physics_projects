def check_nan(i):
    try:
        float(i)
    except ValueError:
        return False
    else:
        return True

def check_empty(i):
    return bool(i)

def get_valid_position():
    """get a valid input, return 'None' when the loop should break"""
    while True:
        position = input("Enter Position: ")
        if position == 'x':
            return None
        elif check_nan(position) and check_empty(position):
            return float(position)
        else:
            print('please enter a valid number')

def get_valid_time(compare_against):
    while True:
        time = input("Enter Time: ")
        if check_nan(time) and check_empty(time):
            time = float(time)
            if time in compare_against:
                print("time can't go backwards")
                continue
            return time
        else:
            print('please enter a valid number')