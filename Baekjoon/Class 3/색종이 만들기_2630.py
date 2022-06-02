import sys
input = sys.stdin.readline

def solve(r1, c1, r2, c2):
    color = paper[r1][c1]
    con = True
    for i in range(r1, r2):
        for j in range(c1, c2):
            if paper[i][j] != color:
                con = False
                break

    if con == True or (r2 - r1 == 1 and c2 - c1 == 1):
        if color == 0:
            ans[0] += 1
        else:
            ans[1] += 1
    else:
        r3 = (r1 + r2) // 2
        c3 = (c1 + c2) // 2
        solve(r1, c1, r3, c3)
        solve(r3, c1, r2, c3)
        solve(r1, c3, r3, c2)
        solve(r3, c3, r2, c2)


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]
solve(0, 0, n, n)
print('\n'.join(map(str, ans)))