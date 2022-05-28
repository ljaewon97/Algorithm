n = int(input())

arr = [0, 1]

for _ in range(n-1):
    arr.append(arr[-1] + arr[-2])

if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    print(2 * (arr[-3] + 2 * arr[-2] + arr[-1]))