w, h, b = map(int, input().split())

res = w * h * b / 8 / 1024 / 1024
print(format(res, '.2f'), 'MB')