for A in range (1, 1001):
    c = 0
    for x in range(1,1001):
        cK = 0
        for y in range (1,1001):
            cY = 0
            for z in range(1,1001):
                
                if ((x + 3*y + 2*z - 54 != 0) or (A < x + 10) or (A < 5*y - 4*x) or (A < z + x)) == True:
                    c += 1
                    cK += 1
                    cY += 1
                else:
                    break
            if cY < 1000:
                break
        if cK < 1000000:
            break
        
    if c == 1000000000:
        print(A)
