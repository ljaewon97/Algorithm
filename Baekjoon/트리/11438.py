# LCA 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 18

n = int(input())
tree = [[] for _ in range(n+1)]
p = [[0] * LOG for _ in range(n+1)]
v = [0] * (n+1)
d = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x, depth):
    v[x] = 1
    d[x] = depth
    for node in tree[x]:
        if v[node] == 1:
            continue
        p[node][0] = x
        dfs(node, depth+1)


dfs(1, 0)
for i in range(1, LOG):
    for j in range(1, n+1):
        p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    
    for i in range(LOG - 1, -1, -1):
        if d[b] >= d[a] + 2 ** i:
            b = p[b][i]

    if a == b:
        return a
    else:
        for i in range(LOG - 1, -1, -1):
            if p[a][i] != p[b][i]:
                a = p[a][i]
                b = p[b][i]
        return p[a][0]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a ,b))