# 나이순 정렬

import sys

n = int(input())
lst = [[] for _ in range(201)]
for _ in range(n):
    temp = input()
    lst[int(temp.split()[0])].append(temp+'\n')

sys.stdout.write(''.join(''.join(i) for i in lst))