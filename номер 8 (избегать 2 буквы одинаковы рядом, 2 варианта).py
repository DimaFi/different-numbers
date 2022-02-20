from itertools import *

kort = permutations('КАПКАН')
slov = set()
count = 0

for x in kort:
    S = ''.join(x)
    if 'АА' not is s and 'КК' not in s and :
        slov.add(s) #сравнит со списком и не внесет повтор
        count += 1

#print(count//2//2)
print(len(slov))
