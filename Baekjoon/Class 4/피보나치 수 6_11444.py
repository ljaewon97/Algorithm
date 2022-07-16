def power(mat, n):
    if n == 1:
        return mat
    if n % 2:
        return multi(power(mat, n-1), mat)
    else:
        return power(multi(mat, mat), n//2)

def multi(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 10 ** 9 + 7
    return res

n = int(input())
mat = [[1, 1], [1, 0]]
print(power(mat, n)[1][0])