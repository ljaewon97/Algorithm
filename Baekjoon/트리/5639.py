# 이진 검색 트리

from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def postorder(start, end):
    if start > end:
        return
    else:
        mid = end + 1
        for i in range(start+1, end+1):
            if num[start] < num[i]:
                mid = i
                break
        postorder(start+1, mid-1)
        postorder(mid, end)
        print(num[start])

num = []

while True:
    try:
        num.append(int(input()))
    except:
        break

postorder(0, len(num)-1)