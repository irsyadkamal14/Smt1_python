import math
def segitigaSiku():
    a = int(input("masukkan sisi : "))
    b = int(input("masukkan sisi berikutnya : "))
    a2 = a**2
    b2 = b**2
    c = math.sqrt(a2 + b2)
    d = c**2
    print(d ," =",a2,"+",b2,"\n hasilnya : ",c)
    return d
segitigaSiku()


import math
def sisi_miring():
    alas_segitiga = int(input("Masukkan nilai alas segitiga: "))
    tinggi_segitiga = int(input("Masukkan nilai tinggi segitiga: "))
    sisi_miring= int(tinggi_segitiga *2 + alas_segitiga **2) *(0.5)
    print(f"Apabila alas segitiga {alas_segitiga} dan tinggi segitiga {tinggi_segitiga} maka sisi miringnya adalah {sisi_miring}")
    return sisi_miring
sisi_miring()