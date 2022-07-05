import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = 0
    m = 0
    n = int(input())
    prices = list(map(int, input().split()))
    temp = []

    while prices:
        cur = prices.pop()
        if cur > m:
            answer += m * len(temp) - sum(temp)
            temp.clear()
            m = cur
        elif cur < m:
            temp.append(cur)
    
    answer += m * len(temp) - sum(temp)
    print(answer)