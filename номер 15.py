for A in range(1, 1001):
    c = 0
    for x in range(1,1001):
        if (((x % A == 0) and (x % 12 == 0)) <= ((x % 42 == 0) or (not(x % 12 == 0)))) == True:
            c +=1
        else:
            break
    if (c == 1000):
        print(A)
