import sys
import copy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = copy.deepcopy(arr)
arr2.sort()
d = dict()
prev = 10 ** 9 + 1
cor = 0
for i in arr2:
    if i != prev:
        d[i] = cor
        cor += 1
        prev = i
for i in range(n):
    print(d[arr[i]], end=' ')