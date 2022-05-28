"""
n = int(input())
arr = []
for _ in range(n):
    arr.append(float(input()))

m = 0

for i in range(n):
    temp = arr[i]
    if temp > m:
        m = temp
    for j in range(i+1, n):
        temp *= arr[j]
        if temp > m:
            m = temp

print("%.3f" % (m))
"""

n = int(input())
arr = [float(input()) for _ in range(n)]
ans = [arr[0]]

for i in range(1, n):
    ans.append(max(ans[-1] * arr[i], arr[i]))

print(f'{max(ans):.3f}')