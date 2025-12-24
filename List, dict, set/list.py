# Contoh
buah = ["apel", "pisang", "mangga"]
angka = [1, 2, 3, 4]
campuran = ["Ndok", 20, True]




# Akses Data
buah = ["apel", "pisang", "mangga"]

print(buah[0])  # apel
print(buah[2])  # mangga

# Dari belakang
print(buah[-1])  # mangga




# Mengubah & Menambah List
buah[1] = "jeruk"      # ubah
buah.append("anggur") # tambah

print(buah)





# Operasi Penting List
len(buah)        # jumlah item
buah.remove("apel")
buah.pop()       # hapus terakhir
