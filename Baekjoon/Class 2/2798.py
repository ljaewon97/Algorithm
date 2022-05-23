# 블랙잭

from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
com = combinations(num, 3)
max_sum = 0

for c in com:
    if max_sum < sum(c) <= m:
        max_sum = sum(c)

print(max_sum)