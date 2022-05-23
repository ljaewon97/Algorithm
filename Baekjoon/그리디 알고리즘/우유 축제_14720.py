n = int(input())
stores = map(int, input().split())
milk = 0
nextMilk = {0:1, 1:2, 2:0}
cnt = 0

for store in stores:
    if store == milk:
        milk = nextMilk[milk]
        cnt += 1

print(cnt)