a, b, c = map(float, input().split())
if a + b > c and b + c > a and a + c > b:
    print("Hop le")
else:
    print("Khong hop le")