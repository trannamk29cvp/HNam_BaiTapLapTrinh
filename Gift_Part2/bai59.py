# Tinh dien tich hinh hoc
import math
def Svuong(canh):
    return canh * canh
def Shcn(dai, rong):
    return dai * rong
def Stron(r):
    return round(r * r * math.pi, 2)
def Stamgiac(a, b, c):
    s = (a + b + c)/2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)


