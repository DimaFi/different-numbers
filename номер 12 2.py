c = 0

s = '1' * 20 + '2' * 15 + 40 * '3'

while ' in s:
    #if '888' in s:
    s = s.replace('25', '9', 1)
    #else:
    #s = s.replace('333', '1', 1)
mas = [int(i) for i in s]
if(sum(mas) == 122):
    print(x)
#print(s.count('8'))
#print(s.count('7'))
#print(s)
#print(c)
