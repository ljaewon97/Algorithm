import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    dist = [float('inf')] * (v+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_dist, cur_dest = heapq.heappop(q)

        if dist[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest]:
            temp = cur_dist + new_dist
            if temp < dist[new_dest]:
                dist[new_dest] = temp
                heapq.heappush(q, (temp, new_dest))
    
    return dist

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

answer = dijkstra(graph, k)
for i in range(1, v+1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i])