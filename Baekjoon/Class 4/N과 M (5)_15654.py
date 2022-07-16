from itertools import permutations

n, m = map(int, input().split())
for comb in permutations(sorted(list(map(int, input().split()))), m):
    print(*comb)