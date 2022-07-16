n, m = map(int, input().split())
if n - m < m:
    m = n - m
up, down = 1, 1
for i in range(m):
    up *= n - i
    down *= i + 1
print(up // down)