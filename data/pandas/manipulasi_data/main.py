import pandas as pd

# tambah kolom
df["status"] = "aktif"

# update nilai
df.loc[df["umur"] < 21, "status"] = "remaja"

# hapus data
df.drop(columns=["umur"])
df.dropna()
