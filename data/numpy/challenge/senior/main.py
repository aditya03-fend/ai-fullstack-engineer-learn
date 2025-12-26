import numpy as np

nilai = np.array(
    [
        [80, 75, 90, 85],
        [60, 70, 65, 68],
        [85, 88, 92, 90],
        [70, 65, 60, 72],
        [90, 95, 88, 94],
        [40, 55, 50, 45],
    ]
)

rata2 = nilai.mean(axis=1)
std_nilai = nilai.std(axis=1)

excellent = np.where(rata2 > 85)[0]
good = np.where((rata2 >= 70) & (rata2 < 85))[0]
at_risk = np.where(rata2 < 70)[0]

mean_global = nilai.mean()
std_global = nilai.std()

outlier_mask = nilai < (mean_global - 2 * std_global)
outlier = nilai[outlier_mask]
jumlah_outlier = outlier.size

print(outlier)
