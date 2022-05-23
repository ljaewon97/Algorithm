# 오큰수

n = int(input())
a = list(map(int, input().split()))
ans = [-1 for _ in range(n)]
stk = []

stk.append(0)
for i in range(n):
    while stk and a[stk[-1]] < a[i]:
        ans[stk.pop()] = a[i]
    stk.append(i)

print(*ans)