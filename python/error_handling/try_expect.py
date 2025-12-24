# Struktur Dasar try except ======================================================================================
try:
    # kode berpotensi error
except:
    # kode jika error terjadi

# Multiple Except ======================================================================================
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Tidak bisa dibagi nol")
except ValueError:
    print("Value error")

# else ======================================================================================
try:
    angka = int("10")
except ValueError:
    print("Error")
else:
    print("Berhasil:", angka)

# finally ======================================================================================
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File tidak ditemukan")
finally:
    print("Proses selesai")

# raise Error ======================================================================================
def tarik_saldo(saldo, jumlah):
    if jumlah > saldo:
        raise ValueError("Saldo tidak cukup")
    return saldo - jumlah
