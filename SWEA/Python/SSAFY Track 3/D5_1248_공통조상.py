from collections import deque

for tc in range(1, int(input()) + 1):
    V, E, n1, n2 = map(int, input().split())
    info = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]
    parent = [0] * (V+1)
    depth = [0] * (V+1)
    for i in range(E):
        parent[info[2*i+1]] = info[2*i]
        tree[info[2*i]].append(info[2*i+1])
    
    d = deque()
    d.append((1, 0))
    while d:
        cur, dep = d.popleft()
        depth[cur] = dep
        for child in tree[cur]:
            d.append((child, dep+1))
    
    while depth[n1] != depth[n2]:
        if depth[n1] < depth[n2]:
            n2 = parent[n2]
        elif depth[n1] > depth[n2]:
            n1 = parent[n1]
    
    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]
    
    def dfs(start):
        global ans
        ans += 1
        for child in tree[start]:
            dfs(child)
    
    ans = 0
    dfs(n1)
    print(f'#{tc} {n1} {ans}')