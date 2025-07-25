n = int(input())
score = 0
for i in range(n):
    diem = float(input())
    score += diem
score /= n
print(f"Diem TB: {score:.2f}, Xep loai: ", end = "")
if score >= 9.0:
    print("Xuat sac")
elif score >= 8.0:
    print("Gioi")
elif score >= 6.5:
    print("Kha")
elif score >= 5.0:
    print("Trung binh")
else:
    print("Yeu")