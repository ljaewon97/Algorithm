# 나머지

mod = []

for _ in range(10):
    mod.append(int(input()) % 42)

print(len(set(mod)))