import random
num = random.randint(1, 100)
while True:
    n = int(input())
    if n < num:
        print("Be hon so can tim")
    elif n > num:
        print("Lon hon so can tim")
    else:
        print("Dung roi")
        break