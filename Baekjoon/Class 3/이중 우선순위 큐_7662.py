import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    v = [0] * k
    maxheap = []
    minheap = []
    
    for i in range(k):
        l, n = input().strip().split()
        n = int(n)

        if l == 'I':
            heapq.heappush(minheap, (n, i))
            heapq.heappush(maxheap, (-n, i))
            v[i] = 1
        elif l == 'D':
            if n == -1:
                while minheap and not v[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    v[minheap[0][1]] = 0
                    heapq.heappop(minheap)
            elif n == 1:
                while maxheap and not v[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    v[maxheap[0][1]] = 0
                    heapq.heappop(maxheap)

    while minheap and not v[minheap[0][1]]:
            heapq.heappop(minheap)
    while maxheap and not v[maxheap[0][1]]:
            heapq.heappop(maxheap)

    if not minheap and not maxheap:
        print('EMPTY')
    else:
        print(-maxheap[0][0], minheap[0][0])