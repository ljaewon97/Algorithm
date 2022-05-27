import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

stk = []
vis = [0] * (n+1)
stk.append([a, 0])
ans = -1

while stk:
    cur, cnt = stk.pop()

    if cur == b:
        ans = cnt
        break

    if vis[cur] == 1:
        continue
    else:
        vis[cur] = 1
        for i in graph[cur]:
            if vis[i] == 0:
                stk.append([i, cnt+1])

print(ans)