# Xử lý chuối
def dem_tu(s):
    count = 0
    lst = s.split(" ")
    return len(lst)
def rev_chuoi(s):
    res = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res
def checkPalin(s):
    motcaigiday = rev_chuoi(s)
    if motcaigiday == s:
        return "Doi xung"
    else:
        return "Khong doi xung"
def chuan_hoa_ten(name):
    lst = name.split(" ")
    res = ""
    for i in lst:
        left = i[0]
        right = i[1:]
        left = left.upper()
        right = right.lower()
        res += left + right + ' '
    return res

s = input()
print(chuan_hoa_ten(s))
    