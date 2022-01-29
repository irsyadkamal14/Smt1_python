ukuran=4
listc=[]
listf=[]
for j in range (0, ukuran+1):
    itemc=j*5
    listc.append(itemc)
    itemf=itemc*(9.0/5.0)+32.0
    listf.append(itemf)
print("Nilai suhu dalam Celcius: ")
print(listc)
print("Nilai suhu dalam Fahremheit: ")
print(listf)