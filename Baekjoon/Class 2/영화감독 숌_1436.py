n = int(input())
x = 0
for i in range(10**7):
    if str(i).find('666') >= 0:
        x += 1
    if n == x:
        print(i)
        break