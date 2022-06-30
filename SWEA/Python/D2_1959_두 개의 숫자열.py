T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    ans = float('-inf')
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(b) < len(a):
        a, b = b, a
    
    for i in range(len(b) - len(a) + 1):
        temp = 0
        for j in range(len(a)):
            temp += a[j] * b[j+i]
        if temp > ans:
            ans = temp
    
    print(f'#{t+1} {ans}')