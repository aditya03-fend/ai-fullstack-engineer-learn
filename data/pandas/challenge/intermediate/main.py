import pandas as pd

produk = {
    "product_id": [1, 2, 3, 4],
    "nama_produk": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "kategori": ["Elektronik", "Aksesoris", "Aksesoris", "Elektronik"],
    "harga": [15000000, 150000, 300000, 2500000],
}

transaksi = {
    "transaksi_id": [101, 102, 103, 104, 105],
    "product_id": [1, 2, 2, 3, 4],
    "qty": [1, 2, 1, 3, 1],
}

df_produk = pd.DataFrame(produk)
df_transaksi = pd.DataFrame(transaksi)

# merge
df_merge = pd.merge(df_produk, df_transaksi, on="product_id", how="inner")

# tambah kolom total harga
df_merge = df_merge.assign(total_harga=lambda x: x.harga * x.qty)

# groupby
total_pendapatan = df_merge.groupby("kategori")["total_harga"].sum()

# terlaris
produk_terlaris = df_merge.groupby("nama_produk")["qty"].sum().idxmax()

# total terbesar
total_terbesar = df_merge.nlargest(1, "total_harga")
