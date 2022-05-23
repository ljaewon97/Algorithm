# 탑

n = int(input())
t = list(map(int, input().split()))
stk = []
ans = []

for i in range(n):
    while stk:
        if stk[-1][1] > t[i]:
            ans.append(stk[-1][0] + 1)
            break
        else:
            stk.pop()
    if not stk:
        ans.append(0)
    stk.append([i, t[i]])

print(' '.join(map(str, ans)))