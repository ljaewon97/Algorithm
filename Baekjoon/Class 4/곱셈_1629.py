a, b, c = map(int, input().split())
arr = []
while True:
    if b % 2:
        arr.append(a)
    if b == 1:
        break
    a = a ** 2 % c
    b //= 2
ans = 1
for i in arr:
    ans *= i
    if ans > c:
        ans %= c
print(ans)