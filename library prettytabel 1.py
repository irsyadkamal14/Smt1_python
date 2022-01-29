# Import Library PrettyTable
from prettytable import PrettyTable

# Buat Object dari PrettyTable()
tabel_data_mahasiswa = PrettyTable()

# Tambahkan Judul Tabel (Table Header)
tabel_data_mahasiswa.field_names = ["NIM", "NAMA", "JURUSAN"]

# Buat variabel penampung data
nim = input("NIM : ")
nama = input("Nama : ")
jurusan = input("Jurusan : ") 

# Menambahkan Data ke Tabel (Table Row)
tabel_data_mahasiswa.add_row(
    [
        nim, nama, jurusan
    ]
)

# Memunculkan data
print(tabel_data_mahasiswa)