t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    up = 1
    down = 1

    for i in range(n):
        up *= m - i
        down *= i + 1

    print(up // down)