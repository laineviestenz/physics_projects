import random
rolls = 10000000
x = 0
got_seven = 0

while x <= rolls:
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if dice_1 + dice_2 == 7:
        got_seven += 1
    x += 1
    if x % 10000 == 0:
        print(x)

print(got_seven/rolls)