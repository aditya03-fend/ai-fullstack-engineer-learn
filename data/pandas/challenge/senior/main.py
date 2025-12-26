import pandas as pd

produk = {
    "product_id": [1, 2, 3, 4],
    "nama_produk": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "kategori": ["Elektronik", "Aksesoris", "Aksesoris", "Elektronik"],
    "harga": [15000000, 150000, 300000, 2500000],
}

transaksi = {
    "transaksi_id": [101, 102, 103, 104, 105, 106],
    "product_id": [1, 2, 2, 3, 4, 2],
    "customer_id": [1, 2, 1, 3, 2, 2],
    "qty": [1, 2, 1, 3, 1, 4],
}

customer = {
    "customer_id": [1, 2, 3],
    "nama_customer": ["Andi", "Budi", "Citra"],
    "kota": ["Jakarta", "Bandung", "Surabaya"],
}

df_produk = pd.DataFrame(produk)
df_transaksi = pd.DataFrame(transaksi)
df_customer = pd.DataFrame(customer)

# merge
df = df_produk.merge(df_transaksi, on="product_id", how="inner").merge(
    df_customer, on="customer_id", how="inner"
)

# tambah kolom
df["total_harga"] = df["harga"] * df["qty"]

# rank
df["rank_transaksi_customer"] = df.groupby("nama_customer")["total_harga"].rank(
    ascending=False, method="dense"
)

# total belanja per customer
total_belanja = df.groupby("nama_customer")["total_harga"].sum()

# rata rata per kota
rata2 = df.groupby("kota")["total_harga"].mean()

# top 1
top_customer = df.groupby("nama_customer")["total_harga"].sum().idxmax()

# terlaris
produk_terlaris = (
    df.groupby(["kategori", "nama_produk"])["qty"]
    .sum()
    .reset_index()
    .sort_values(["kategori", "qty"], ascending=[True, False])
    .groupby("kategori")
    .first()
)

print(produk_terlaris)
