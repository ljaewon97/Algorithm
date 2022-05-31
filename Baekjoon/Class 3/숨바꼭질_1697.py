from collections import deque

def bfs():
    d = deque()
    d.append(n)

    while d:
        x = d.popleft()
        if x == k:
            print(dist[x])
            break

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[x] + 1
                d.append(i)

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

bfs()