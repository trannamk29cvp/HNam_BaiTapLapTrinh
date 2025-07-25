n = int(input())
res = ""
while n != 0:
    res += str(n % 2)
    n//=2
    
temp = ""
for i in range(len(res) - 1, -1, -1):
    temp += res[i]
print(temp)
