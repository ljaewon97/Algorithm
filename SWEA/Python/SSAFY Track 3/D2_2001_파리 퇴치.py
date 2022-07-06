T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    ans = 0
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(m):
                for l in range(m):
                    temp += board[i+k][j+l]
            if temp > ans:
                ans = temp
    
    print(f'#{t+1} {ans}')
