a = []

def f(x, n):
    global a
    if (n == 8):
        if x not in a and x in range(1000, 1024):
            a.append(x)
        return 1
    elif (n > 8):
        return 0
    elif (n < 8):
        return f(x + 1, n + 1) + f(x + 5, n + 1) + f(x * 3, n + 1)

print(f(1, 0))
print(a)
