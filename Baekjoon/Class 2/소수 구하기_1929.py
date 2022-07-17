m, n = map(int, input().split())
arr = [1] * (n+1)
arr[0] = arr[1] = 0
for i in range(2, n+1):
    for j in range(2*i, n+1, i):
        arr[j] = 0
for i in range(m, n+1):
    if arr[i]:
        print(i)