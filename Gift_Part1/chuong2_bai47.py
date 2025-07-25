mon, yeah = map(int, input().split())
if mon == 2:
    if yeah % 4 == 0 and (yeah % 100 != 0 or yeah % 400 == 0):
        print(29)
    else:
        print(28)
if mon in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif mon != 2:
    print(30)
    