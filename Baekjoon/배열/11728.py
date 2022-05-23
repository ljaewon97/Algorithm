N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)
for i in range(len(C)):
    print(C[i], end=' ')