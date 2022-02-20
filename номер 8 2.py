from itertools import *

mas = permutations('КЛАБХАУС')

c = 0

for x in mas:
    s = ''.join(x)
    if 'AA' not in s:
        c += 1
    if (c < 1000):
        print(c, s)
print(c//2)
