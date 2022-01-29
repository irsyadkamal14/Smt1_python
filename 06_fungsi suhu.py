def konversi_F (listC):
    listF = []
    ukuran = len(listC)
    for j in range (0, ukuran):
        itemF =  listC[j]*(9.0/5.0)+32.0
        listF.append(itemF)
    return listF

    
c= [0, 5, 10, 15, 20, 25, 30,40, 45, 50, 55]
f= konversi_F(c)
print("Nilai suhu dalam celcius: ")
print(c)
print("Nilai suhu dalam farenhit: ")
print(f)
