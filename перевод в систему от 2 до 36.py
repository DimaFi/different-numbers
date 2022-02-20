def f(n, a):
    c1 = ''
    c = ''
    if a < 10:
        while n > 0:
            c = str(c) + str(n % a)
            n = n // a
    elif a > 10:
        while n > 0:
            p = n % a
            if p < 10:
                c = str(c) + str(n % a)
            elif p >= 10:
                p = p + 55
                c = str(c) + str(chr(p))
            n = n // a        
    c1 = c[::-1]
    print(c1)
    
f(256, 16)
