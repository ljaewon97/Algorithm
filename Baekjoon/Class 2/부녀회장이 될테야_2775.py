for _ in range(int(input())):
    k = int(input())
    n = int(input())
    apart = [[i for i in range(n+1)]]
    for floor in range(1, k+1):
        temp = [0]
        sum = 0
        for room in range(1, n+1):
            sum += apart[floor-1][room]
            temp.append(sum)
        apart.append(temp)

    print(apart[k][n])