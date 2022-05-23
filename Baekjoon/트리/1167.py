# 트리의 지름

import sys
sys.setrecursionlimit(100000)

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp), 2):
        if temp[i] != -1:
            tree[temp[0]].append([temp[i], temp[i+1]])

def dfs(x, w):
    for i in tree[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = b + w
            dfs(a, b + w)

distance = [-1 for _ in range(v+1)]
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))

distance = [-1 for _ in range(v+1)]
distance[start] = 0
dfs(start, 0)

print(max(distance))