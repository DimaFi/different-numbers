from itertools import *

kort = product('ЕЛЕЙ', repeat = 6)

count = 0

for x in kort:
    s = ''.join(x)
    if s[0] != 'Й' and s[5] != 'Й' and x.count('Й') <= 1 and 'ЙЕ' not in s and  'ЕЙ' not in s:
        #print(s)
        count += 1

print(count//4)

