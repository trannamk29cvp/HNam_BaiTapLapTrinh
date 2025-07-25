def check(n):
    div = 0
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            div += i
            if n//i != i and i != 1:
                div += n//i
    return div == n

n = int(input())
if check(n):
    print("La so hoan hao")
else:
    print("Khong phai so hoan hao")
        