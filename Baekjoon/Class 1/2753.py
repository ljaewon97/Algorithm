# 윤년

y = int(input())

if y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
        print(0)
    else:
        print(1)
else:
    print(0)