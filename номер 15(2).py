for A in range (1, 1001):
    c = 0
    for k in range(1,1001):
        cK = 0
        for n in range (1,1001):
            if ((5*k + 6*n > 57) or ((k <= A) and (n <A))) == True:
                c += 1
                cK += 1
            else:
                break
        if cK < 1000:
            break
    if c == 1000000:
        print(A)
