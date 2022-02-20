from itertools import *

mas = permutations('НИГРОЛ')

c = 0

for x in mas:
    s = ''.join(x)
    if s[0] != 'О' and 'ОИГ' not in s:
        c += 1
        print(c, s)
