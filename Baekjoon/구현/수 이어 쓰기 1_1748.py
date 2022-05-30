n = int(input())
dig = len(str(n))
ans = 0
for i in range(dig-1, -1, -1):
    temp = n - 10 ** i + 1
    n -= temp
    ans += temp * (i+1)

print(ans)