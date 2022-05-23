# 올바른 배열

def checkNumber(arr, num):
    idx = arr.index(num)
    temp1 = temp2 = 4
    for i in range(1, 5):
        if (num - i) in arr:
            temp1 -= 1
        if (num + i) in arr:
            temp2 -= 1
    return min(temp1, temp2)

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

res = []
for i in range(N):
    res.append(checkNumber(arr, arr[i]))

print(min(res))