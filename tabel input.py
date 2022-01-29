
from prettytable import PrettyTable

tabel_suhu = PrettyTable()
tabel_suhu.field_names = [
    "NO",
    "  SUHU C  ",
    "  SUHU F  "
]

def suhuF (suhu_f):
    konfersi = (((suhu_f*9)/5)+32) 
    return konfersi

nomor = 0
for i in range (-20, 40, 5) :
    nomor += 1
    tabel_suhu.add_row(
    [
        nomor, i, suhuF(i)
    ]
    )

print(tabel_suhu)
