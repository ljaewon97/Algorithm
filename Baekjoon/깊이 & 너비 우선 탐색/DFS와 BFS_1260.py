from collections import deque

def dfs(start):
    stk = []
    visited = [0] * (n+1)
    stk.append(start)

    while stk:
        cur = stk.pop()
        if visited[cur] == 0:
            visited[cur] = 1
            print(cur, end=' ')

        for node in graph[cur]:
            if visited[node] == 0:
                stk.append(node)
        

def bfs(start):
    d = deque()
    visited = [0] * (n+1)
    d.append(start)
    visited[start] = 1

    while d:
        cur = d.popleft()
        print(cur, end=' ')

        for node in graph[cur]:
            if visited[node] == 0:
                d.append(node)
                visited[node] = 1


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i] = sorted(graph[i], reverse=True)

dfs(v)
print()

for i in range(n+1):
    graph[i] = sorted(graph[i])

bfs(v)