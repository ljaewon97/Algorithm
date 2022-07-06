T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    ans = 0
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        hor, ver = 0, 0
        for j in range(n):
            if board[i][j] == 1:
                hor += 1
            else:
                if hor == k:
                    ans += 1
                hor = 0
            
            if board[j][i] == 1:
                ver += 1
            else:
                if ver == k:
                    ans += 1
                ver = 0

            if j == n - 1 and hor == k:
                ans += 1
            if j == n - 1 and ver == k:
                ans += 1
    
    print(f'#{t+1} {ans}')