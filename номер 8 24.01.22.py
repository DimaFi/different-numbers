from itertools import *

mas = product('СЛОН', repeat = 5)
count = 0

for x in mas:
    if x.count('С') >= 1:
        count += 1
        
print(count)
