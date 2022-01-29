banyak_skor= int(input("Banyak skor setiap siswa : "))
skor_lagi="Y"

while skor_lagi=="Y":
    print("Masukkan skor")
    total=0
    for i in range (1, banyak_skor +1):
        skor=int(input("Ujian", i,":"))
        total=total+skor
    rerata=total/banyak_skor
    print("Rerata adalah ",rerata)
    skor_lagi=input("Masukkan skor untuk siswa lain (Y/T)? ")
    skor_lagi=skor_lagi.upper()