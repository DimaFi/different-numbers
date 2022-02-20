mx = 0 
count = 0 

for x in range(3466, 9081):
    c = ''
    a = x
    while a > 0:
        c = str(c) + str(a % 8)
        a = a // 8
    if (len(c) != len(str(x))) and (x % 7 == 1 or x % 7 == 5):
        count += 1
        if x > mx:
            mx = x

print(count)
print(mx)
