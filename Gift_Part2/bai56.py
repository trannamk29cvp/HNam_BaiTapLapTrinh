# Kiem tra chan le
def check(n):
    if n % 2 == 0:
        return "Chan"
    else:
        return "Le"
n = int(input())
print(check(n))
    