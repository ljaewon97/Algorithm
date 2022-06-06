def solution(places):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    answer = []
    
    def check(place, r, c, dis):
        vis.append([r, c])
        if place[r][c] == 'P' and dis > 0:
            res.append(1)
        if dis == 2:
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] in ['O', 'P'] and [nr, nc] not in vis:
                check(place, nr, nc, dis + 1)
                
    for place in places:
        res = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    vis = []
                    check(place, i, j, 0)
                    if res:
                        break
        
        answer.append(0) if res else answer.append(1)

    return answer