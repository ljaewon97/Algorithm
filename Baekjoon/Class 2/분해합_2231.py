def digitSum(num):
    sum = num
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

n = int(input())
for i in range(1, n):
    if digitSum(i) == n:
        print(i)
        break
else:
    print(0)