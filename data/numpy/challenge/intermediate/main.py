import numpy as np

nilai = np.array([[80, 75, 90], [60, 70, 65], [85, 88, 92], [70, 65, 60], [90, 95, 88]])

rata2_siswa = nilai.mean(axis=1)

rata2_mapel = nilai.mean(axis=0)

rata2_tinggi = rata2_siswa.argmax()

remidial = nilai[nilai < 70]

jumlah_nilai_remidial = remidial.size
print(jumlah_nilai_remidial)
