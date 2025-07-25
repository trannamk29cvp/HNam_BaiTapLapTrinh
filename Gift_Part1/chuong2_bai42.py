n = int(input())
money = 0
if n >= 1:
    money += 15000
if n >= 2:
    money += 12000 * (min(n, 5) - 2 + 1)
if n >= 6:
    money += 10000 * (n-5)
print(money)