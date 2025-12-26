import pandas as pd

data = {
    "produk": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"],
    "kategori": ["Elektronik", "Aksesoris", "Aksesoris", "Elektronik", "Aksesoris"],
    "harga": [15000000, 150000, 300000, 2500000, 150000],
    "qty": [1, 2, 1, 1, 3],
}

df = pd.DataFrame(data)


# Tampilkan 5 baris awal
df.head()

# tambah kolom total harga
df.loc[:, "total_harga"] = df["harga"] * df["qty"]


# filtering
df_transaksi = df.query("kategori == 'Aksesoris' and qty >= 2")


# total 1 kolom
total_pendapatan = df["total_harga"].sum()


# rata rata per kategori
df.groupby("kategori")["harga"].agg(["mean", "count"])
