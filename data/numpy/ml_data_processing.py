import numpy as np

data = np.array([150, 160, 170, 180])

normalized = (data - data.min()) / (data.max() - data.min())
print(normalized)
