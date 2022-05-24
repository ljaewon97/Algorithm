import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, c):
    if 0 <= r < h and 0 <= c < w:
        if m[r][c] != 1:
            return
        else:
            m[r][c] = 2
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0:
                        continue
                    else:
                        dfs(r + i, c + j)
    else:
        return
    

while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    cnt = 0
    m = []
    for _ in range(h):
        m.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)