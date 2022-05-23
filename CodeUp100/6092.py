n = int(input())
called = list(map(int, input().split()))
count = [0 for _ in range(23)]

for i in range(n):
    count[called[i]-1] += 1

for i in range(23):
    print(count[i], end=' ')