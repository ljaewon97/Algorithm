ans = [0] * (10**6 + 1)
ans[0] = -1
n = int(input())

for i in range(1, min(n, 10**6) + 1):
    if i % 6 == 0:
        ans[i] = min(ans[i//3], ans[i//2], ans[i-1]) + 1
    elif i % 3 == 0:
        ans[i] = min(ans[i//3], ans[i-1]) + 1
    elif i % 2 == 0:
        ans[i] = min(ans[i//2], ans[i-1]) + 1
    else:
        ans[i] = ans[i-1] + 1

print(ans[n])