import heapq
import sys
input = sys.stdin.readline

n = int(input())
neg = []
pos = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not neg and not pos:
            print(0)
        elif not neg:
            print(heapq.heappop(pos))
        elif not pos:
            print(-heapq.heappop(neg))
        else:
            if neg[0] <= pos[0]:
                print(-heapq.heappop(neg))
            else:
                print(heapq.heappop(pos))
    else:
        if x > 0:
            heapq.heappush(pos, x)
        else:
            heapq.heappush(neg, -x)