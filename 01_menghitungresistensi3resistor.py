print("__________Menghitung Resistensi 3 Resistor__________\n")
a = int(input('Masukkan Nilai Resistor 1 Seri : '))
b = int(input('Masukkan Nilai Resistor 2 Pararel : '))
c = int(input('Masukkan Nilai Resistor 3 Pararel : '))

d = b*c
e = ((d/b)*1) + ((d/c)*1)

for i in range(1, 100):
      if ((e % i == 0) and (d % i == 0)):
            f = i  
g = e/f
h = d/f
j = h/g
k = a+j
print("\nNilai resitor yang kamu masukkan : ", a,' , ', b,' , ', c)
print("Total nilai  R2 + R3 adalah : ",j)
print("Total nilai resistor tersebut : ", k)



