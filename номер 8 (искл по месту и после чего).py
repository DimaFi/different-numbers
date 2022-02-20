from itertools import *

mas = permutations('РУЛЬКА')

c = 0

for x in mas:
    s = ''.join(x)
    if s[0] != 'Ь' and 'УЬ' not in s and 'АЬ' not in s:
        c += 1
        print(c, s)
