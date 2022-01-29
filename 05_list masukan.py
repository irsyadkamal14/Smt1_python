print("____+++ Menampilkan Inputan Array +++____\n")
lista = []

while(True):
    
    masukkan = int(input("Masukkan Angka Bulat : "))
    if masukkan == 0:
        break
    lista.append(masukkan)
print("Nilai yang dimasukkan : ", lista)