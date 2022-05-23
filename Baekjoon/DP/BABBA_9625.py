k = int(input())
arr = [1, 0]
for _ in range(k):
    arr[0], arr[1] = arr[1], arr[0] + arr[1]

print(*arr)