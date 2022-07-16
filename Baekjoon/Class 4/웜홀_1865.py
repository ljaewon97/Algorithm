import sys
input = sys.stdin.readline

def bf():
    MAX = 10 ** 9
    dist = [MAX] * (n+1)
    dist[1] = 0

    for i in range(n):
        for j in range(2*m + w):
            cur_node = roads[j][0]
            next_node = roads[j][1]
            time = roads[j][2]
            if dist[next_node] > dist[cur_node] + time:
                dist[next_node] = dist[cur_node] + time
                if i == n - 1:
                    return True
    
    return False


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    roads = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        roads.append((s, e, t))
        roads.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        roads.append((s, e, -t))
    
    print('YES' if bf() else 'NO')