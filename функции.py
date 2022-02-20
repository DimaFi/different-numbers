def f(n, a):
    c1 = ''
    c = ''
    while n > 1:
        c = str(c) + str(n % a)
        n = n // a
    c1 = c[::-1]
    print(c1)
    
f(20, 8)
