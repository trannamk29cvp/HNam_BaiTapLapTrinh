# Hàm tìm kiếm và sắp xếp
def tim_max_min(lst):
    ma = -1000000000000000000000000000
    mi = 1000000000000000000000000000
    for i in lst:
        ma = max(ma, i)
        mi = min(mi, i)
    print(f"So lon nhat: {ma}, So be nhat: {mi}")
def findPos(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            print(i)
            break
def BubbleSort(lst):
    for i in range(len(lst)-1, -1, -1):
        for j in range(i):
            if lst[j] >= lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
def SelectSort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] <= lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
        
# print(SelectSort([3, 7, 1, 9, 5]))