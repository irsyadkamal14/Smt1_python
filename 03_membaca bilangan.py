print("____+++ Membaca Sebuah Integer (+/-) +++____\n")

angka = int(input("Masukkan Angka : "))
print("_____________________")

if (angka % 2) == 0:
    print("Angka ",angka, " Termasuk Bilangan Genap" )
    if angka == 0 :
        print("Nilainya Kosong")
    elif angka >= 0 :
        print("Nilainya Positif")
    else :
        print("Nilainya Negatif")
    print("__________________")
else :
    print("Angka ",angka, " Termasuk Bilangan Ganjil" )
    if angka == 0 :
        print("Nilainya Kosong")
    elif angka >= 0 :
        print("Nilainya Positif")
    else :
        print("Nilainya Negatif")
    print("__________________")
