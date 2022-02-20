from itertools import *

mas = permutations('ВОРОТА')

c = 0

krot = set()

for x in mas:
    s = ''.join(x)
    if 'ОА' not in s and 'АО' not in s and 'ОО' not in s:
        c += 1
        print(s)
print(c//2)
