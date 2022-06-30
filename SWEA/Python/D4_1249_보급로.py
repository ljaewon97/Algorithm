import heapq

def dijkstra(routes, sr, sc, n):
    dist = [[float('inf')] * n for _ in range(n)]
    dist[sr][sc] = 0
    queue = []
    heapq.heappush(queue, (dist[sr][sc], (sr, sc)))
    
    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)
        cr, cc = cur_dest
        
        if dist[cr][cc] < cur_dist:
            continue
            
        for new_dest, new_dist in routes[cr][cc]:
            temp = new_dist + cur_dist
            nr, nc = new_dest
            if temp < dist[nr][nc]:
                dist[nr][nc] = temp
                heapq.heappush(queue, (temp, (nr, nc)))
    
    return dist

T = int(input())
di = [-1,1,0,0]
dj = [0,0,-1,1]
for t in range(T):
    n = int(input())
    map = []
    for _ in range(n):
        temp = []
        i = input()
        for char in i:
            temp.append(int(char))
        map.append(temp)
    
    routes = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = []
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    temp.append([(ni, nj), map[ni][nj]])
            routes[i][j] = temp
    
    ans = dijkstra(routes, 0, 0, n)
    print(f'#{t+1} {ans[n-1][n-1]}')