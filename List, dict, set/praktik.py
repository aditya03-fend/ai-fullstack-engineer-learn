# Data Dari API
users = [
    {"nama": "Andi", "umur": 20},
    {"nama": "Budi", "umur": 25}
]

print(users[0]["nama"])



# Praktik Wajib
mahasiswa = [
    {"nama": "Ani", "umur": 20},
    {"nama": "Budi", "umur": 22},
    {"nama": "Ani", "umur": 20}
]

nama_unik = set()

for mhs in mahasiswa:
    nama_unik.add(mhs["nama"])

print(nama_unik)

