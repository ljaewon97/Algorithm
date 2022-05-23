import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def blind(r, c, k):
    color = pic[r][c]
    pic[r][c] = dict1[color] if k == 0 else 0

    for i in range(4):
        new_r, new_c = r + dr[i], c + dc[i]
        if 0 <= new_r < n and 0 <= new_c < n:
            if pic[new_r][new_c] == color:
                blind(new_r, new_c, k)


n = int(input())
pic = [list(input().rstrip()) for _ in range(n)]
dict1 = {'R': 'r', 'G': 'r', 'B': 'b'}
colors = [['R', 'G', 'B'], ['r', 'b']]
cnt = [0, 0]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for k in range(2):
    for i in range(n):
        for j in range(n):
            if pic[i][j] in colors[k]:
                blind(i, j, k)
                cnt[k] += 1

print(*cnt)