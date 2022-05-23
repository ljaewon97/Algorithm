# 배열 돌리기 4

from itertools import permutations
from copy import deepcopy

def rotateArr(arr, r, c, s):
    for i in range(s):
        x, y = r-s-1+i, c-s-1+i
        prev = arr[x][y]

        for j in range(c-s+i, c+s-i):
            y = j
            temp = arr[x][y]
            arr[x][y] = prev
            prev = temp

        for j in range(r-s+i, r+s-i):
            x = j
            temp = arr[x][y]
            arr[x][y] = prev
            prev = temp

        for j in range(c+s-2-i, c-s-2+i, -1):
            y = j
            temp = arr[x][y]
            arr[x][y] = prev
            prev = temp   

        for j in range(r+s-2-i, r-s-2+i, -1):
            x = j
            temp = arr[x][y]
            arr[x][y] = prev
            prev = temp

    return arr


def valueArr(arr):
    s = []
    for row in arr:
        s.append(sum(row))
    
    return min(s)


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

rotate = []
for _ in range(K):
    rotate.append(list(map(int, input().split())))

p = list(permutations(rotate, len(rotate)))

a = []
for case in p:
    c = deepcopy(A)
    for r in list(case):
        c = rotateArr(c, r[0], r[1], r[2])
    a.append(valueArr(c))

print(min(a))