# 두 배열의 합

from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_dict = defaultdict(int)
B_dict = defaultdict(int)

A_sum = []
for i in range(1, n+1):
    for j in range(0, n+1-i):
        A_dict[sum(A[j:j+i])] += 1

B_sum = []
for i in range(1, m+1):
    for j in range(0, m+1-i):
        B_dict[sum(B[j:j+i])] += 1

cnt = 0

for key in A_dict.keys():
    cnt += A_dict[key] * B_dict[T - key]

print(cnt)