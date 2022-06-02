t = int(input())
arr = [1, 2, 4]
for _ in range(7):
    arr.append(arr[-1] + arr[-2] + arr[-3])
for _ in range(t):
    print(arr[int(input())-1])