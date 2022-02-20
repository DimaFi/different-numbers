def f(x, p):
    if (x == p):
        return 1
    elif (int(x, 2) > int(p, 2)):
        return 0
    else:
        return f(bin(int(x, 2) + 1)[2:], p) + f('1' + x, p)

print(f('100', '110001'))

#print(int(10, 2))
