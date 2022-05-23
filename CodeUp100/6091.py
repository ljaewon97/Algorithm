a, b, c = map(int, input().split())
m = max(a, b, c)
ans = m

while True:
    if ans % a == 0 and ans % b == 0 and ans % c == 0:
        break
    else:
        ans += m

print(ans)