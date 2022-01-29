jum = 0.0
Bil_Mak = int(input ("Masukkan jumlah data input: "))
for penghitung_loop in range(1, Bil_Mak+1) :
    nilai_masuk = float(input ("Masukkan bilangan: "))
    if nilai_masuk > 0.0 :
        jum = jum + nilai_masuk
        print ("Nilai penghitung: ", penghitung_loop)
print ("Nilai jumlah: ", jum)