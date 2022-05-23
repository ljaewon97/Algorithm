a, b = input().split()

a = a.replace('6', '5')
b = b.replace('6', '5')
mi = int(a) + int(b)

a = a.replace('5', '6')
b = b.replace('5', '6')
ma = int(a) + int(b)

print(mi, ma)