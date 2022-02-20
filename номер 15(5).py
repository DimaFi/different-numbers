for A in range (1, 1001):
    c = 0
    for x in range (1,1001):
        if ((x & A != 0) and (x & 41 == 0) and (x & 37 == 0)) == False:
            c += 1
        else:
            break
    if c == 1000:
        print(A)
