import numpy as np

gambar = np.array([
    [255, 255, 255],
    [0,   0,   0],
    [255, 255, 255]
])

# invert warna
invert = 255 - gambar
print(invert)
