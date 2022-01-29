print("____+++ Merubah Celcius Menjadi Farenheit____\n")

a = float(-20)
while a <= 40 :
    print("Nilai C :", a, "=", "Nilai F :" ,(((a*9)/5)+32))
    a += 5

def fah(nilai):
    hasil = (nilai *9/5)+32
    return hasil

nomer = 1
for i in range(-20,45,5):
    print(nomer," ","nilai ",i,"\t  jika C : ",i,"\t maka F nya :",fah(i))
    nomer += 1