from itertools import *

mas = product('ВЕКНО' , repeat = 5)

c = 0

for x in mas:
    s = ''.join(x)
    c += 1
    if x.count('Н') == 2 and x.count('К') == 2:
        print(c, s)
