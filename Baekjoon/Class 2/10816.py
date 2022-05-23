# 숫자 카드 2

n = int(input())
cards = list(map(int, input().split()))
counts = dict()
m = int(input())
nums = list(map(int, input().split()))

for num in cards:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(' '.join(str(counts[i]) if i in counts else '0' for i in nums))