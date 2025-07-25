a, b, c = map(float, input().split())
s = (a + b + c) / 2
dientich = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"{round(dientich, 1)}")