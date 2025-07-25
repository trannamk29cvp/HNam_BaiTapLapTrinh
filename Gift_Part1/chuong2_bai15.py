import math
def checkPrime(n):
    for i in range(2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if checkPrime(n):
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")

