def f(n):
    return (n % 10 == 0 or n % 10 == 1)

def f2(n):
    return n <= 126 and n >= -127

print(f(751))
print(f2(-12))
