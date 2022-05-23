# LCA

from collections import deque

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0 for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
depth[1] = 1
d = deque()
d.append(1)

while d:
    cur = d.popleft()
    de = depth[cur]

    for node in tree[cur]:
        if depth[node] == 0:
            depth[node] = de + 1
            d.append(node)
            parent[node] = cur

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))