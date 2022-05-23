n = int(input())

arr = []
arr.append(0)
arr.append(1)

for i in range(2,1500001):
    arr.append((arr[i-2]+arr[i-1])%1000000)

print(arr[n%1500000])
