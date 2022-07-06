for tc in range(1, int(input()) + 1):
    n = int(input())
    stk = list(map(int, input().split()))
    temp = []
    m, ans = 0, 0

    while stk:
        cur = stk.pop()
        if cur > m:
            ans += m * len(temp) - sum(temp)
            temp.clear()
            m = cur
        elif cur < m:
            temp.append(cur)
    
    ans += m * len(temp) - sum(temp)
    print(f'#{tc} {ans}')