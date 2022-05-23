# 창고 다각형
import copy

n = int(input())
cor = []
area = 0
top = []

for _ in range(n):
    temp = list(map(int, input().split()))
    cor.append(temp)
    temp2 = copy.deepcopy(temp)
    temp2[0] += 1
    cor.append(temp2)

t = max(i[1] for i in cor)
cor.sort()
corl = list(reversed(copy.deepcopy(cor)))

x = cor[-1][0]
y = cor[-1][1]

while(True):
    if len(cor) == 0:
        break

    if cor[-1][1] == t:
        top.append(cor[-1])

    if cor[-1][1] <= y:
        cor.pop()
    else:
        area += (x - cor[-1][0]) * y
        x = cor[-1][0]
        y = cor[-1][1]

x = corl[-1][0]
y = corl[-1][1]

while(True):
    if len(corl) == 0:
        break

    if corl[-1][1] <= y:
        corl.pop()
    else:
        area += (corl[-1][0] - x) * y
        x = corl[-1][0]
        y = corl[-1][1]


area += (top[0][0] - top[-1][0]) * t

print(area)