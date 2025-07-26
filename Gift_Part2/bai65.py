# Hàm quản lý dữ liệu học sinh
def add_student(lst, name, age, score):
    hoc_sinh = {
        "ten": name,
        "tuoi": age,
        "diem": score
    }
    lst.append(hoc_sinh)

# list_hs = []
# add_student(list_hs, "Nam", 15, 49.9)
# 
# print(list_hs[0]["diem"])

def find_student(lst, name):
    for A in lst:
        if A["ten"] == name:
            return {
                "ten": name,
                "tuoi": A["tuoi"],
                "diem": A["diem"]
            }
    return{
        "ten": "not found",
        "tuoi": "not found",
        "diem": "not found"
    }

def xep_loai_hs(diem):
    if diem >= 9.0:
        return "Xuat sac"
    elif diem >= 8.0:
        return "Gioi"
    elif diem >= 6.5:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"
    
def sort_by_score(lst):
    score = []
    new_lst = []
    added_name = []
    for A in lst:
        score.append(A["diem"])
    score = sorted(score)
    for i in score:
        for A in lst:
            if A["diem"] == i and A["name"] not in added_name:
                new_lst.append({
                    "ten": A["ten"],
                    "tuoi": A["tuoi"],
                    "diem": i
                })
                added_name.append(A["name"])
                break
    
    return new_lst