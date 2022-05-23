# 카드1

from collections import deque

n = int(input())
card = deque(range(1, n+1))
arr = []

while len(card) > 1:
    arr.append(card.popleft())
    card.append(card.popleft())

arr.append(card[0])

for i in range(len(arr)):
    print(arr[i], end=' ')