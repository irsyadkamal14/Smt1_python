import math
def sisi_S (list_s):
    lists=[]
    for j in range (0, 2) :
        nilai = list_s[j]**2
        lists.append(nilai)
    hasil = math.sqrt(lists[0]+lists[1])
    return hasil


listsisi= []
i = 0
print("Masukkan 2 sisi pendek : ")
while(True):
    i += 1
    sisi = int(input("Sisi %d : " %(i)))
    listsisi.append(sisi)
    if i == 2:
        break
print("Sisi 1 dan sisi 2 adalah : {},{} " .format(listsisi[0], listsisi[1]))


a = sisi_S (listsisi)
print("Diketahui sisi miringnya adalah : ",a)