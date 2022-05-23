com = int(input())
n = int(input())
network = [[] for _ in range(com+1)]
for _ in range(n):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0 for _ in range(com+1)]
stk = []
stk.append(1)

while stk:
    cur = stk.pop()
    visited[cur] = 1

    for node in network[cur]:
        if visited[node] == 0:
            stk.append(node)

print(sum(visited)-1)