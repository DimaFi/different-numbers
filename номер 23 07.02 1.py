def f(x, p):
    if (x == p):
        return 1
    elif (x > p):
        return 0
    elif (x < p):
        return f(x * 2, p) + f(x * 3, p)

print(f(8, 96) * f(96, 3456))
