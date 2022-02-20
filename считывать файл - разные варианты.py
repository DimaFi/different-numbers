f = open('23.txt', 'r')

s = f.readline()

s = f.readlines()

mas = [int(x) for x in f.readlines()]

mas = [int(x) for x in f.readline().split()]
