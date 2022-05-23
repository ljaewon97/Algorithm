# 최대공약수와 최소공배수

a, b = map(int, input().split())
arr = [a, b]

while True:
    if arr[-2] % arr[-1] == 0:
        break
    else:
        arr.append(arr[-2] % arr[-1])

m = arr[-1]
print(m)
print(a * b // m)