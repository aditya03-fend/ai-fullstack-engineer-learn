import numpy as np

nilai_siswa = [65, 70, 80, 90, 55, 75, 85, 60]

nilai = np.array(nilai_siswa)

rata2 = nilai.mean()
max = nilai.max()
min = nilai.min()

lulus = nilai[nilai >= 75]

total_lulus = (nilai >= 75).sum()
