# Hàm mô phỏng trò chơi
import random
def tung_xu(so_lan):
    sap, ngua = 0, 0
    for i in range(so_lan):
        face = random.randint(0, 1)
        if face == 0:
            sap += 1
        else:
            ngua += 1
    print(f"sap: {sap}, ngua: {ngua}")
        
# tung_xu(100)

def tung_tung_sahur(face, time):
    result = []
    for i in range(time):
        x_face = random.randint(1, face)
        result.append(x_face)
    return result

# print(tung_tung_sahur(6, 10))

def doan_so(min_val, max_val):
    #so_can_tim = n
    n = random.randint(min_val, max_val)
    times = 0
    while True:
        num = int(input("Bạn đoán: "))
        if num < n:
            print("Số bạn đoán nhỏ hơn số cần tìm")
        elif num > n:
            print("Số bạn đoán lớn hơn số cần tìm")
        else:
            print(f"Bạn đã đoán đúng sau {times} lần")
            break
        times += 1
        
# doan_so(1, 100)


            
            
            