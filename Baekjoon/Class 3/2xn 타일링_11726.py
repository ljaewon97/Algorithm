n = int(input())
a, b = 1, 2
for _ in range(n-1):
    a, b = b % 10007, (a + b) % 10007
print(a)