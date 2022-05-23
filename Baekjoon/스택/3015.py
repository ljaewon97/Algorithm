# 오아시스 재결합

n = int(input())
stk = []
ans = 0

for _ in range(n):
    h = int(input())
    while stk and stk[-1][0] < h:
        ans += stk.pop()[1]

    if stk and stk[-1][0] == h:
        cnt = stk.pop()[1]
        ans += cnt
        if stk:
            ans += 1
        stk.append((h, cnt+1))
    else:
        if stk:
            ans += 1
        stk.append((h, 1))

print(ans)