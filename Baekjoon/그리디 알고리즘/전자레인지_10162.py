t = int(input())

buttons = [0, 0, 0]
idx = 0

for i in [300, 60, 10]:
    temp = t // i
    buttons[idx] += temp
    t -= temp * i
    idx += 1

if t == 0:
    print(' '.join(map(str, buttons)))
else:
    print(-1)