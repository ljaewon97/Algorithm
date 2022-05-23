n, m = map(int, input().split())
fl = []
vis = [[False]*m for _ in range(n)]
cnt = 0

for _ in range(n):
    temp = []
    line = input()
    for l in line:
        temp.append(l)
    fl.append(temp)

for i in range(n):
    for j in range(m):
        if vis[i][j]:
            continue
        else:
            cnt += 1
            if fl[i][j] == '-':
                c = j
                vis[i][j] = True
                while True:
                    c += 1
                    if c >= m: break
                    if fl[i][c] == '|':
                        break
                    else:
                        vis[i][c] = True
            elif fl[i][j] == '|':
                r = i
                vis[i][j] = True
                while True:
                    r += 1
                    if r >= n: break
                    if fl[r][j] == '-':
                        break
                    else:
                        vis[r][j] = True

print(cnt)