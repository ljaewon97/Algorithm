import heapq
import sys

n=int(sys.stdin.readline())
minhq=[]
maxhq=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if len(minhq)==len(maxhq):
        heapq.heappush(maxhq,-x)
    else:
        heapq.heappush(minhq,x)

    if minhq and minhq[0]<-maxhq[0]:
        mx=-heapq.heappop(maxhq)
        mn=heapq.heappop(minhq)
        heapq.heappush(maxhq,-mn)
        heapq.heappush(minhq,mx)
    print(-maxhq[0])