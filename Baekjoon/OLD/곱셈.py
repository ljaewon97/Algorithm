a = int(input())
b = int(input())

b1 = b % 10
b10 = int((b % 100) / 10)
b100 = int(b / 100)

print(a * b1)
print(a * b10)
print(a * b100)
print(a * b)