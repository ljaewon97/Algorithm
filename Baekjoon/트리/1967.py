# 트리의 지름

import sys
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

def dfs(x, wei):
    for i in tree[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = b + wei
            dfs(a, wei + b)

distance = [-1 for _ in range(n+1)]
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))

distance = [-1 for _ in range(n+1)]
distance[start] = 0
dfs(start, 0)

print(max(distance))