# 소수 찾기

num = [1 for _ in range(1001)]
pn = []

for i in range(2, 1001):
    if num[i] == 0:
        continue
    else:
        pn.append(i)
        for j in range(i, 1001, i):
            num[j] = 0

pn = set(pn)
n = int(input())
cnt = 0

for i in map(int, input().split()):
    if i in pn:
        cnt += 1

print(cnt)