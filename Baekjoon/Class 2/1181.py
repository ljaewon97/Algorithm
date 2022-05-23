# 단어 정렬

from collections import deque

n = int(input())
word = [[] for _ in range(51)]
queue = deque(['z99'])

for _ in range(n):
    temp = input()
    word[len(temp)].append(temp)

for i in range(len(word)):
    if word[i]:
        word[i].sort()
        # word[i] = set(word[i])
        for w in word[i]:
            if w != queue[-1]:
                print(w)
                queue.append(w)

