import numpy as np

users = np.array([[25, 5, 3], [30, 2, 5], [22, 6, 1], [40, 1, 10]])
# [umur, jam_belajar, pengalaman_tahun]

weights = np.array([0.2, 0.5, 1.0])

skor = users @ weights
print(skor)
