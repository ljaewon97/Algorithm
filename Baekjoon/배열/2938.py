# 3으로 나누어 떨어지지 않는 배열

N = int(input())
lst = list(map(int, input().split()))
arr = [[] for _ in range(3)]

for num in lst:
    mod = num % 3
    arr[mod].append(num)

ans = []

if (len(arr[0]) == 0 and len(arr[1]) != 0 and len(arr[2]) != 0) or (len(arr[0]) > ((N+1) // 2)):
    print(-1)
else:
    while len(arr[1]) != 0:
        if len(arr[0]) > 1:
            ans.append(arr[0].pop(0))
        ans.append(arr[1].pop(0))

    if len(arr[0]) != 0:
        ans.append(arr[0].pop(0))

    while len(arr[2]) != 0:
        ans.append(arr[2].pop(0))
        if len(arr[0]) > 0:
            ans.append(arr[0].pop(0))

    for num in ans:
        print(num, end=' ')