mx = 0
count = 0
for x in range(1305, 14064):
    if (x % 2 == 0 or x % 3 == 0) and (x % 7 != 0) and (x % 11 != 0) and (x % 17 != 0) and (x % 23 != 0):
        count += 1
        if x > mx:
            mx = x

print(mx)
print(count)
