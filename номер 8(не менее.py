from itertools import *

mas = product('РУСТАМ' , repeat = 6)

c = 0

for x in mas:
    s = ''.join(x)
    if x.count('Р') + x.count('С') + x.count('Т') + x.count('М') >= 3:
        c += 1
print(c)
