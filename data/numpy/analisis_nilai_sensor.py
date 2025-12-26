import numpy as np

suhu = np.array([30.1, 30.3, 29.9, 31.5, 45.0])

rata2 = suhu.mean()
anomali = suhu[suhu > 40]

print("Rata-rata:", rata2)
print("Anomali:", anomali)
