s = input()

arr = [0, 0]
cur = s[0]
arr[int(cur)] += 1

for i in s:
    if i == cur:
        continue
    else:
        cur = i
        arr[int(cur)] += 1

print(min(arr))