def square_root(n, precision):
    root = n/2
    for k in range(precision):
        root = 1/2*(root + (n/root))
    print(root)

square_root(16, 5)

for i in range(15):
    square_root(17, i)