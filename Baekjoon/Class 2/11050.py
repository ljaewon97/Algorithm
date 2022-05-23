# 이항 계수 1

import sys

n, k = map(int, sys.stdin.readline().split())

a, b = 1, 1

for i in range(n, n-k, -1):
    a *= i

for i in range(1, k+1):
    b *= i

print(int(a / b))