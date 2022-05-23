h, b, c, s = map(int, input().split())

res = h * b * c * s / 8 / 1024 / 1024
print(format(res, '.1f'), 'MB')