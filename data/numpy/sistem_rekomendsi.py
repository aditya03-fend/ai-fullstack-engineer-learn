import numpy as np

rating = np.array([
    [5, 4, 0],
    [3, 0, 4],
    [0, 2, 5]
])

# rata-rata rating tiap produk
avg_produk = rating.mean(axis=0)
print(avg_produk)
