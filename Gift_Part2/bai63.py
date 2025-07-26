# Xử lí danh sách nâng cao
def evenNum(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result
# print(evenNum([2, 3, 6, 10]))
def trans_List(lst, function):
    for i in lst:
        i = function(i)
    return lst
def list_and_cond(lst, cond):
    result = []
    for i in lst:
        if cond(i):
            result.append(i)
    return result
def thongke(lst):
    # trung binh cong, trung vi, value xuat hien nhieu nhat
    n = len(lst)
    s = sum(lst) / n
    lst = sorted(lst)
    if n % 2 == 0:
        trungvi = (lst[n//2 - 1] + lst[n // 2]) // 2
    else:
        trungvi = lst[n//2]
    
    freq = [0] * 10**5
    max_freq = 0
    max_value = 0
    for i in lst:
        freq[i] += 1
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_value = i
    print(f"Trung Binh Cong: {s:.2f}, Trung Vi: {trungvi}, Gia Tri Xuat Hien Nhieu Nhat: {max_value}")

        
    