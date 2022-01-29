print("____+++ Penilaian Skor Pertandingan +++____\n")

a = int(input("Masukkan Skor Pertandingan TIM A : "))
b = int(input("Masukkan Skor Pertandingan TIM B : "))
if a >= b :
    print("\nTIM A Menang")
    print("____________________")
elif a <= b :
    print("\nTIM B Menang")
    print("____________________")
else :
    print("\nPermainan Seri")
    print("____________________")