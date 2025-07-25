n = int(input())
temp = n
# reverse n
rev = 0
while n != 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if rev == temp:
    print("Doi xung")
else:
    print("Khong doi xung")