def findIdx(num):
    cnt = -1
    for i in range(n):
        if line[i] == 0:
            cnt += 1
            if cnt == num:
                return i

n = int(input())
arr = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    line[findIdx(arr[i])] = i + 1

print(' '.join(map(str, line)))