from itertools import *

mas = product('0123456789' , repeat = 3)

c = 0

for x in mas:
    s = ''.join(x)
    if s[0] <= s[1] and s[1] <= s[2] and s[0] != '0':
        c += 1
print(c)
