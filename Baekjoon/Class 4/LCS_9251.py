a = input()
b = input()
lcs = [[0] * (len(b)+1) for _ in range((len(a) + 1))]
for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        elif a[i-1] != b[j-1]:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[len(a)][len(b)])