# 두 개의 배열

def binary(item, B, start, end):
    diff = end - start
    if diff <= 1:
        return start
    mid = (start + end) // 2
    if item < B[mid]:
        return binary(item, B, start, mid)
    else:
        return binary(item, B, mid, end)


def findMin(lst):
    curr = lst[2]
    res = 2
    if lst[1] <= curr:
        curr = lst[1]
        res = 1
    if lst[0] <= curr:
        curr = lst[0]
        res = 0
    return res


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    s = 0
    for item in A:
        loc = binary(item, B, 0, m)
        lst = []
        lst.append(abs(B[loc-1] - item))
        lst.append(abs(B[loc] - item))
        lst.append(abs(B[(loc+1)%m] - item))
        idx = findMin(lst)
        s += B[loc + idx - 1]

    print(s)