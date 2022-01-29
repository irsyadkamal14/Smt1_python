deret = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 100, 10, 11, 11, 11]

print("\nakses list per indeks: ")
print(deret[1])
print(deret[5])
print(deret[10])


print("\nmencacah isi list: ")
for x in deret:
    print (x)


print("\npanjang list: " + str(len(deret)))


print("\nbanyaknya angka 11: " + str(deret.count(11)))  


print("\nmenambah elemen list dengan append:")


deret.append(15)
deret.append(16)
deret.append(17)
deret.append(18)
deret.append(19)
deret.append(20)
print(deret)


print("\nmencari indeks suatu nilai dengan index: ")


print(deret.index(100))
print(deret.index(15))
print(deret.index(10))
print(deret.index(17))


print("\nmenambah elemen list dengan insert:")


deret.insert(2, 35)
deret.insert(2, 36)
deret.insert(2, 37)
deret.insert(2, 38)
deret.insert(2, 39)
deret.insert(2, 30)
print(deret)


print("\nmembuang elemen list dengan pop:")


deret.pop()
deret.pop()
deret.pop()
print(deret)


print("\nmembuang elemen list dengan remove:")


deret.remove(35)
deret.remove(36)
deret.remove(37)
deret.remove(38)
deret.remove(39)
deret.remove(30)
print(deret)


print("\nmenambah elemen list dengan extend:")


deret2 = [1, 2, 3, 4, 5]
deret.extend(deret2)


print(deret)


print("\nmembalik list dengan reverse:")
deret.reverse()
print(deret)


print("\nmengurut list dengan sort:")
deret.sort()
print(deret)


print("\nmencari nilai max dari list:")
print(max(deret))


print("\nmencari nilai min dari list:")
print(min(deret))


print("\nmencari nilai sum dari list:")
print(sum(deret))

