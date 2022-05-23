n = int(input())
called = list(map(int, input().split()))

called_reverse = called[::-1]

for i in range(n):
    print(called_reverse[i], end=' ')