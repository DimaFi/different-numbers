a = []

def f(x, n):
    global a
    if (n == 8):
        if x not in a:
            a.append(x)
        return 1
        
    elif (n > 8):
        return 0
    elif (n < 8):
        return f(x * 8, n + 1) + f(x // 2, n + 1)

print(f(512, 0))
print(a)
