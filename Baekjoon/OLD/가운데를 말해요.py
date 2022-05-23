import heapq
import sys

input = sys.stdin.readline
N = int(input())

left, right, answer = [], [], []

for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and (-left[0]) > right[0]:
        temp1 = -heapq.heappop(left)
        temp2 = heapq.heappop(right)
        heapq.heappush(left, -temp2)
        heapq.heappush(right, temp1)

    answer.append(-left[0])
        
for i in range(N):
    print(answer[i])