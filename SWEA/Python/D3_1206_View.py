for tc in range(1, 11):
    n = int(input())
    b = list(map(int, input().split()))
    ans = 0
    i = 2

    while i < n - 2:
        if b[i] == max(b[i-2:i+3]):
            ans += b[i] - max(b[i-2], b[i-1], b[i+1], b[i+2])
            i += 3
        else:
            i += 1
    
    print(f'#{tc} {ans}')