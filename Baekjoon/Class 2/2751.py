# 수 정렬하기 2

import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

print('\n'.join(map(str, arr[:])))