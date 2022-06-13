from collections import deque

def solution(board):
    n = len(board)
    dp = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    dp[0][0] = [0, float('inf'), 0, float('inf')]
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    
    def bfs():
        d = deque()
        d.append((0, 0, 0, 0))
        d.append((0, 0, 2, 0))
        
        while d:
            r, c, dir, cost = d.popleft()
            
            if r == c == n - 1:
                continue
                
            for i in range(4):
                ncost = cost + 100
                if i != dir:
                    ncost += 500
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                    if ncost < dp[nr][nc][i]:
                        dp[nr][nc][i] = ncost
                        d.append((nr, nc, i, ncost))
                        
    bfs()
    return min(dp[n-1][n-1])