A = []
for i in range (1, 1001):
    A.append(i)
    c = 0
    for x in range (1,1001):
        if (((x in A) <= (x*x <= 64)) and ((x*x <= 25) <= (x in A))) == True:
            c += 1
        else:
            break
    if c == 1000:
        print(i)
