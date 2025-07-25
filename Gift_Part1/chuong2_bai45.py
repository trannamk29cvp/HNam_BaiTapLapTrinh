a, b = map(int, input().split())
# a, b = b, a % b
temp2 = b
temp3 = a
while b != 0:
    temp = a
    a = b
    b = temp % b
ucln = a
bcnn = (temp3 * temp2) // ucln
print(f"UCLN: {a}, BCNN: {bcnn}")