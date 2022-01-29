from random import randint
angel = 0
while True:
    bil = randint(0, 10)
    print(bil), angel <= bil
    angel += 1
    
    if bil == 5:
        break
print("Jumlah Perulangan : ", angel)