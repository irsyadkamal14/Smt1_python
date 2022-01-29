print("____+++ Predikat Nilai +++____\n")

print("Nilai Yang Dapat Di Masukkan A, A+, B+, B-, C+, C-, D, E")

lanjut = 'Y'
while lanjut == 'Y':
    huruf = input("Masukkan Kategori Nilai mu : ")
    if huruf == 'A' or huruf == 'a':
        print("_____________")
        print("4,00")
    elif huruf == 'A-' or huruf == 'a-':
        print("_____________")
        print("3,75")
    elif huruf == 'B+' or huruf == 'b+':
        print("_____________")
        print("3,50")
    elif huruf == 'B-' or huruf == 'b-':
        print("_____________")
        print("2,75")
    elif huruf == 'C+' or huruf == 'c+':
        print("_____________")
        print("2,50")
    elif huruf == 'C' or huruf == 'c':
        print("_____________")
        print("2,00")
    elif huruf == 'D' or huruf == 'd':
        print("_____________")
        print("1,00")
    elif huruf == 'E' or huruf == 'e':
        print("_____________")
        print("0,00")
    else :
        print("Key yang anda masukkan salah")
    lanjut = input("\nApakah Ingin Mengulangi (Y/T) : ")
    lanjut = lanjut.upper()
    print("________________________________\n")
