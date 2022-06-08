def rotate(array):
    res = []
    n = len(array)
    
    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(array[j][i])
        res.append(temp)
    return res


def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    targets = 0
    for i in range(n):
        targets += lock[i].count(0)
    
    for _ in range(4):
        blocks = []
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    blocks.append((i, j))
                    
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                cnt = targets
                con = True
                for block in blocks:
                    r, c = block
                    r, c = r + i, c + j
                    if 0 <= r < n and 0 <= c < n:
                        if lock[r][c] == 0:
                            cnt -= 1
                        elif lock[r][c] == 1:
                            con = False
                if con and cnt == 0:
                    return True
        
        key = rotate(key)
    
    return False