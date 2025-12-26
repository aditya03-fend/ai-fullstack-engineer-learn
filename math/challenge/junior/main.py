import numpy as np

user = [30, 4, 2]
# [umur, jam_belajar, pengalaman_tahun]

weights = [[0.2], [0.5], [1.0]]

X = np.array(user)
W = np.array(weights)

Y = X @ W
print(f"Skor kelayakan user = {(Y[0])}")
