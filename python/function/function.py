# Struktur Function ======================================================================================
def nama_function(parameter):
    # kode
    return hasil

# Function with Param ======================================================================================
def sapa(nama):
    print("Halo", nama)

sapa("Ndok")
sapa("Andi")

# Function dengan Return ======================================================================================
def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print(hasil)


# Defautl Param ======================================================================================
def sapa(nama="User"):
    print("Halo", nama)

sapa()
sapa("Ndok")


# Function + List + Dict ======================================================================================
def cek_stok(produk):
    if produk["stok"] > 0:
        return "Tersedia"
    return "Habis"

produk = {"nama": "Laptop", "stok": 5}
print(cek_stok(produk))
