from itertools import *

mas = permutations('УЛЕЙ', 4)

count = 0

for x in mas:
    s = ''.join(x)
    if s[0] != 'Й' and 'ЕУ' not in s:
        print(x, ' === > ' s)
        count += 1

print(count)
