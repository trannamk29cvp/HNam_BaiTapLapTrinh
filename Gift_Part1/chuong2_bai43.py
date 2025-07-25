a, b = map(float,input().split())
if a == 0:
    if b == 0:
        print("Vo so nghiem")
    else:
        print("Vo nghiem")
else:
    print(f"x = {-b / a}")