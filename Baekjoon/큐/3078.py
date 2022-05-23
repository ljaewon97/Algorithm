# 좋은 친구

from collections import deque

n, k = map(int, input().split())
name = [len(input()) for _ in range(n)]
cnt = 0
ques = [deque() for _ in range(21)]

for i in range(len(name)):
    while ques[name[i]] and i - ques[name[i]][0] > k:
        ques[name[i]].popleft()
    if ques[name[i]]:
        cnt += len(ques[name[i]])
    ques[name[i]].append(i)

print(cnt)