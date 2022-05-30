n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
v = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if v[i] == 0:
        cnt += 1
        stk = []
        stk.append(i)

        while stk:
            cur = stk.pop()
            if v[cur] == 1:
                continue
            v[cur] = 1
            for node in graph[cur]:
                if v[node] == 0:
                    stk.append(node)

print(cnt)