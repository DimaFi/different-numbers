s = input()
s1 = s[::-1]
if s1[:4] == 'lmth' or s1[:3] == 'mth' or s1[:3] == 'php':
    print('это веб-страница')

else:
    print('что-то другое')
