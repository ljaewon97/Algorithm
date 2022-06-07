from collections import deque

def solution(m, n, board):
    answer = 0
    da = [1, 0, 1]
    db = [0, 1, 1]
    
    for i in range(m):
        board[i] = list(board[i])
    
    def check(r, c):
        v = []
        d = deque()
        d.append([r, c])
        v.append([r, c])
        while d:
            a, b = d.popleft()
            if (0 <= a < m-1 and 0 <= b < n-1) and (board[a][b] == board[a+1][b] == board[a][b+1] == board[a+1][b+1]):
                for i in range(3):
                    na, nb = a + da[i], b + db[i]
                    if [na, nb] not in v:
                        d.append([na, nb])
                        v.append([na, nb])
        return v

    def fall(c):
        cnt = 0
        for i in range(m-1, 0, -1):
            for j in range(i, 0, -1):
                if board[j][c] == 0 and board[j-1][c] != 0:
                    board[j][c], board[j-1][c] = board[j-1][c], board[j][c]
                    cnt += 1
        return cnt

    while True:
        cnt = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0:
                    v = check(i, j)
                    if len(v) > 1:
                        for cor in v:
                            board[cor[0]][cor[1]] = 0

        for i in range(n):
            cnt += fall(i)
    
        if cnt == 0:
            break
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1

    return answer