c1 = 0
summ = 0
c = 0
mas = []
for x in range(2020, 647038):
    t = str(x)
    s = 0
    mx = 9
    x1 = x
    for j in range(0, len(t)):
        if int(t[j]) < mx:
            mx = int(t[j])
    while x1 > 0:
        #print(type(t))
        s += x1 % 10
        x1 = x1 // 10
    if int(t[0]) != mx and int(t[1]) != mx and int(t[2]) != mx and s < 10:
        c += 1
        summ += x
        mas.append(int(t))
        
print(summ/c)
check = 10**100
count = 0
for x in mas:
    if abs(x - (summ/c)) < check:
        check = abs(x - (summ/c))
        count = x
print(c)
print(count)
