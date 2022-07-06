from collections import deque

t = 1
while True:
    try:
        length, start = map(int, input().split())
    except:
        break

    arr = list(map(int, input().split()))
    ma = max(arr)
    dist = [0] * (ma + 1)
    v = [0] * (ma + 1)
    contact = [[] for _ in range(ma + 1)]
    for i in range(0, length, 2):
        contact[arr[i]].append(arr[i+1])
    
    d = deque()
    d.append((start, 0))
    v[start] = 1

    while d:
        cur, step = d.popleft()
        dist[cur] = step

        for i in contact[cur]:
            if not v[i]:
                v[i] = 1
                d.append((i, step+1))
    
    ans = 0
    maxStep = 0
    for i in range(len(dist)):
        if dist[i] >= maxStep:
            maxStep = dist[i]
            ans = i
    
    print(f'#{t} {ans}')
    t += 1