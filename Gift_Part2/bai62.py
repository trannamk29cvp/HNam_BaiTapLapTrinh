# Đệ quy
def fib_dequy(n):
    if n <= 1:
        return n
    return fib_dequy(n-1) + fib_dequy(n-2)
def luythua(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return luythua(a, n // 2) * luythua(a, n // 2)
    else:
        return luythua(a, n // 2) * luythua(a, n // 2) * a
def revStr(s):
    if len(s) <= 1:
        return s
    return s[-1] + revStr(s[:-1])
def gcd_dequy(a, b):
    if b == 0:
        return a
    return gcd_dequy(b, a%b)

# print(gcd_dequy(12, 4))