# 단어순서 뒤집기

n = int(input())

for i in range(n):
    s = input().split()
    ans = ''
    for j in range(len(s)-1, -1, -1):
        ans += s[j] + ' '

    print(f'Case #{i+1}: {ans}')