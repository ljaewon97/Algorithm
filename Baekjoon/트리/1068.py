# 트리

''' 99%에서 틀림
from collections import defaultdict
from collections import deque

def delNode(root):
    d = deque()
    d.append(root)

    while d:
        a = d.popleft()
        if a in tree:
            while tree[a]:
                d.append(tree[a].pop())


def countLeaf(root):
    if len(tree[root]) == 0:
        answer[root] += 1
    else:
        for i in tree[root]:
            countLeaf(i)


n = int(input())
tree = defaultdict(list)

temp = list(map(int, input().split()))
for i in range(len(temp)):
    tree[temp[i]].append(i)

root = tree[-1][0]
r = int(input())
tree[temp[r]].remove(r)
delNode(r)

answer = [0 for _ in range(n)]
countLeaf(root)
answer[root] = 0
print(sum(answer))
'''

n = int(input())
arr = list(map(int, input().split()))
num = int(input())

def dfs(num, arr):
    arr[num] = -2
    for i in range(n):
        if arr[i] == num:
            dfs(i, arr)

dfs(num, arr)
answer = 0

for i in range(n):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)