# 알파벳 찾기

s = input()
arr = [-1 for _ in range(26)]

for i in range(26):
    arr[i] = s.find(chr(ord('a') + i))

for i in arr:
    print(i, end=' ')