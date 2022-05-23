a, b, c = map(int, input().split())

for num in [a, b, c]:
    if num % 2 == 0:
        print('even')
    else:
        print('odd')