import sys
input = sys.stdin.readline

S = 0
M = int(input())
for _ in range(M):
    command = input().split()
    if command[0] == 'add':
        x = int(command[1])
        S |= (1 << x)
    elif command[0] == 'remove':
        x = int(command[1])
        S &= ~(1 << x)
    elif command[0] == 'check':
        x = int(command[1])
        print(1 if S & (1 << x) != 0 else 0)
    elif command[0] == 'toggle':
        x = int(command[1])
        S ^= (1 << x)
    elif command[0] == 'all':
        S = (1 << 21) - 1
    else:
        S = 0