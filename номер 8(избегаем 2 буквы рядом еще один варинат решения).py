def Check(x):
    for i in range(len(x) - 1):
        if x[i] == x[i+1]:
            return False
    return Rtue



from itertools import permutations
slov = {x for x in purmutations('КАПКАН') if Check(x)}
    #if x[0] != x[1] and ...
print(len(slov))
