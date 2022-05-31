import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x : (x[1], x[0]))

last = 0
cnt = 0
for meeting in meetings:
    if last <= meeting[0]:
        cnt += 1
        last = meeting[1]

print(cnt)