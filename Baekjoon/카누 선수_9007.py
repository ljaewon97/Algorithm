import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    arr = []

    for _ in range(4):
        arr.append(list(map(int, input().split())))
    
    a1, a2 = [], []
    for i in range(n):
        for j in range(n):
            a1.append(arr[0][i] + arr[1][j])
            a2.append(arr[2][i] + arr[3][j])
    
    a1.sort()
    a2.sort()

    i, j = 0, len(a2) - 1
    diff = float('inf')
    ans = 0

    while i < len(a1) and j >= 0:
        if abs(a1[i] + a2[j] - k) < diff:
            diff = abs(a1[i] + a2[j] - k)
            ans = a1[i] + a2[j]
        
        if abs(a1[i] + a2[j] - k) == diff:
            if a1[i] + a2[j] < ans:
                ans = a1[i] + a2[j]
        
        if a1[i] + a2[j] > k:
            j -= 1
        elif a1[i] + a2[j] < k:
            i += 1
        else:
            break

    if i < len(a1) and j >= 0:
        if abs(a1[i] + a2[j] - k) < diff:
            diff = abs(a1[i] + a2[j] - k)
            ans = a1[i] + a2[j]
    
    print(ans)