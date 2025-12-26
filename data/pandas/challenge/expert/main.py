import pandas as pd
import numpy as np

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
df["total_belanja"] = df.groupby("nama_customer")["total_harga"].transform("sum")

# rata rata per kota
rata2_kota = df.groupby("kota")["total_harga"].mean()

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

# log total harga
df["log_total_harga"] = df["total_harga"].transform(lambda x: np.log(1 + x))

rata2 = df["total_harga"].mean()

# transaksi besar
df["is_big_transaction"] = (df["total_harga"] > df["total_harga"].mean()).astype(int)

# total belanja customer
df["customer_total_spend"] = df.groupby("customer_id")["total_harga"].transform("sum")

# rata rata
df["customer_avg_spend"] = df.groupby("customer_id")["total_harga"].transform("mean")

# rank global
customer_rank = (
    df.groupby("customer_id")["total_harga"]
      .sum()
      .rank(ascending=False, method="dense")
)

df["customer_rank_global"] = df["customer_id"].map(customer_rank)

# persentase
df["pct_of_customer_spend"] = (df["total_harga"] / df["total_belanja"]) * 100

# ubah kolom
df["kategori"] = df["kategori"].astype("category")

# tabel baru
df_customer = (
    df.groupby(["nama_customer", "kota"])["total_harga"]
    .agg(total_spend="sum", avg_spend="mean")
    .reset_index()
)

df_customer["rank"] = (
    df_customer["total_spend"].rank(ascending=False, method="min").astype(int)
)

df_customer = df_customer.sort_values("rank")

print(df_customer)
