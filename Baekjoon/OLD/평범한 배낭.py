N, K = map(int, input().split())

items = [[0, 0]]

for _ in range(N):
    a, b = map(int, input().split())
    items.append([a, b])

bag = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W = items[i][0]
        V = items[i][1]

        if j < W:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(V + bag[i-1][j-W], bag[i-1][j])


print(bag[N][K])