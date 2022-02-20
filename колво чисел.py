def f(n):
    s = ''
    while n > 0:
        s = str(s) + str(n % 2)
        n = n // 2        
    return s.count('0')

print(f(75))
