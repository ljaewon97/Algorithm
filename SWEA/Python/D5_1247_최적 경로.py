from itertools import permutations

def dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

T = int(input())

for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1])
    home = (arr[2], arr[3])
    clients = []
    for i in range(4, len(arr), 2):
        clients.append((arr[i], arr[i+1]))
    ans = float('inf')
    for case in permutations(clients, n):
        d = 0
        d += dist(home, case[0])
        for i in range(n-1):
            d += dist(case[i], case[i+1])
        d += dist(case[-1], company)
        if d < ans:
            ans = d
    print(f'#{t+1} {ans}')