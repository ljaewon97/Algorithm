n = int(input())
a = 0
b = 1
c = 1
for _ in range(n-1):
    c = a + b
    a = b
    b = c

print(c)