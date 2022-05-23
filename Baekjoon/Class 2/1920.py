# 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
num = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

for a in arr:
    print(1 if a in num else 0)