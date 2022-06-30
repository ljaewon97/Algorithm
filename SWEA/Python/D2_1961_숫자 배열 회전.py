def rotate90(arr):
    res = []
    n = len(arr)
    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(arr[j][i])
        res.append(temp)
    
    return res


T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    print(f'#{t+1}')
    arr90 = rotate90(arr)
    arr180 = rotate90(arr90)
    arr270 = rotate90(arr180)
    ans = [arr90, arr180, arr270]
    for i in range(n):
        for j in range(3):
            print(''.join(map(str, ans[j][i])), end=' ')
        print()
