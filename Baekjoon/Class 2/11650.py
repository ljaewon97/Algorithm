# 좌표 정렬하기

n = int(input())
coords = []

for _ in range(n):
    coords.append(list(map(int, input().split())))

coords.sort()
for c in coords:
    print(' '.join(map(str, c[:])))