n = int(input())
fib = [0, 1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i])
for i in range(0, n):
    print(fib[i], end = " ")