import sys
input = sys.stdin.readline

def cutTree(h):
    sum = 0
    for tree in trees:
        if tree > h:
            sum += tree - h
    return sum


n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    if cutTree(mid) < m:
        end = mid - 1
    elif cutTree(mid) > m:
        start = mid + 1
    else:
        start += 1
        end += 1
    
print(mid-1)