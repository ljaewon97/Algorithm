import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bug(r, c):
    ground[r][c] = 2

    for i in range(4):
        new_r, new_c = r + dr[i], c + dc[i]
        if 0 <= new_r < n and 0 <= new_c < m:
            if ground[new_r][new_c] == 1:
                bug(new_r, new_c)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        ground[b][a] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                bug(i, j)
                cnt += 1

    print(cnt)