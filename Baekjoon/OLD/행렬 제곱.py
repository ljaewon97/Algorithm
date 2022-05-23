N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def matrix_mul(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    
    if B % 2 == 1:
        temp = [[0 for _ in range(N)] for _ in range(N)]
        C = matrix_mul(A, B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += C[i][k] * A[k][j]
                temp[i][j] %= 1000
        return temp

    else:
        temp = [[0 for _ in range(N)] for _ in range(N)]
        C = matrix_mul(A, B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += C[i][k] * C[k][j]
                temp[i][j] %= 1000
        return temp


result = matrix_mul(A, B)

for line in result:
    for element in line:
        print(element, end=' ')
    print()