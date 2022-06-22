def solution(n, build_frame):
    def checkb(r, c):
        if (r > 0 and wall[r-1][c][0]) or (r > 0 and c < n and wall[r-1][c+1][0]) or (wall[r][c-1][1] and wall[r][c+1][1]):
            return True
        return False

    def checkp(r, c):
        if wall[r][c][1] or (c > 0 and wall[r][c-1][1]) or r == 0 or wall[r-1][c][0]:
            return True
        return False

    def deletecheck():
        for c in range(n):
            for r in range(n):
                if wall[r][c][1] and not checkb(r, c):
                    return False
                if wall[r][c][0] and not checkp(r, c):
                    return False
        return True    

    answer = []
    wall = [[[0] * 2 for _ in range(n+1)] for _ in range(n+1)]

    for command in build_frame:
        c, r, t, com = command
        if com == 1:
            if t == 0:
                if checkp(r, c):
                    wall[r][c][0] = 1
            else:
                if checkb(r, c):
                    wall[r][c][1] = 1
        else:
            if t == 0:
                wall[r][c][0] = 0
                if not deletecheck():
                    wall[r][c][0] = 1
            else:
                wall[r][c][1] = 0
                if not deletecheck():
                    wall[r][c][1] = 1

    for c in range(n+1):
        for r in range(n+1):
            if wall[r][c][0]:
                answer.append([c,r,0])
            if wall[r][c][1]:
                answer.append([c,r,1])

    return answer