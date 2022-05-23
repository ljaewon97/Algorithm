# 숫자의 개수

num = 1
arr = [0 for _ in range(10)]

for _ in range(3):
    num *= int(input())

for i in str(num):
    arr[int(i)] += 1

for i in arr:
    print(i)