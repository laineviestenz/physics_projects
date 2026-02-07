def check_nan(input):
    try:
        float(input)
    except ValueError:
        return False
    else:
        return True

def check_empty(input):
    return bool(input)

# def check_valid(input):
#     a = check_nan(input)
#     b = check_empty(input)
#     return input if a*b == 1 