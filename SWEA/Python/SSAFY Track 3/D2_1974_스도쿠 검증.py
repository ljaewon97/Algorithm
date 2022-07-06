T = int(input())
for t in range(T):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    
    ans = 0
    conh, conv, conb = True, True, True
    
    for i in range(9):
        h, v = set(), set()
        for j in range(9):
            if puzzle[i][j] in h:
                conh = False
            h.add(puzzle[i][j])
            if puzzle[j][i] in v:
                conv = False
            v.add(puzzle[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b = set()
            for k in range(3):
                for l in range(3):
                    if puzzle[i+k][j+l] in b:
                        conb = False
                    b.add(puzzle[i+k][j+l])
    
    if conh and conv and conb:
        ans = 1
    print(f'#{t+1} {ans}')