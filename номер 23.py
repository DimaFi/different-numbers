def f(x, p):
    if (x == p):
        return 1
    elif (x > p or x == 11 or x == 12):
        return 0
    elif (x < p):
        return f(x + 1, p) + f(x + 2, p) + f(x + 3, p)

print(f(1, 9) * f(9, 30))

