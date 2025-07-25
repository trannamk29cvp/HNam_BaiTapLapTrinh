yeah = int(input())
if yeah % 4 == 0 and (yeah % 100 != 0 or yeah % 400 == 0):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")