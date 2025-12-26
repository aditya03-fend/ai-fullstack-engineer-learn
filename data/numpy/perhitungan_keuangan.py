import numpy as np

harga = np.array([100, 102, 101, 105, 110])

return_harian = np.diff(harga) / harga[:-1]
print(return_harian)
