a, b = map(int, input().split())
temp = 0
while b != 0:
    temp = a
    a = b
    b = temp % b
print(a)
