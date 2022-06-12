import heapq

def solution(n, s, a, b, fares):
    def dijkstra(graph, start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        queue = []
        heapq.heappush(queue, (dist[start], start))
        
        while queue:
            cur_dist, cur_dest = heapq.heappop(queue)
            
            if dist[cur_dest] < cur_dist:
                continue
                
            for new_dest, new_dist in graph[cur_dest]:
                temp = new_dist + cur_dist
                if temp < dist[new_dest]:
                    dist[new_dest] = temp
                    heapq.heappush(queue, (temp, new_dest))
        
        return dist
    
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    min_fare = [[]]
    for i in range(1, n+1):
        min_fare.append(dijkstra(graph, i))
    
    answer = min_fare[s][a] + min_fare[s][b]
    for i in range(1, n+1):
        if i == s:
            continue
        cost = min_fare[s][i] + min_fare[i][a] + min_fare[i][b]
        if cost < answer:
            answer = cost
    
    return answer