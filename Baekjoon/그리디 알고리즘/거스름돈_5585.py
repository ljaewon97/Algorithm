price = int(input())
exchange = 1000 - price
num = 0

for coin in [500, 100, 50, 10, 5, 1]:
    n = exchange // coin
    exchange -= n * coin
    num += n

print(num)