for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            if ((a and not c) or (not a and b and c)) != 2:
                print(a, ' ', b, ' ', c)
